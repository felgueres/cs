import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM, 
    TrainingArguments, 
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, TaskType
import pandas as pd
from datasets import Dataset
import wandb

import warnings
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL.*")


# Initialize wandb
wandb.init(
    project="gsm8k-step-by-step",
    name="gemma-2b-lora",
    config={
        "model": "google/gemma-2b",
        "lora_rank": 16,
        "lora_alpha": 32,
        "learning_rate": 2e-4,
        "batch_size": 8,
        "effective_batch_size": 16,
        "epochs": 3
    }
)

print("Loading GSM8K data...")
train_df = pd.read_csv("papers/01_lets_verify_step_by_step/processed_gsm8k/train.csv")
test_df = pd.read_csv("papers/01_lets_verify_step_by_step/processed_gsm8k/test.csv")

# Convert to HF datasets
train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

print(f"Train examples: {len(train_dataset)}")
print(f"Test examples: {len(test_dataset)}")

# Load tokenizer and model
print("Loading Gemma-2B with LoRA...")
model_name = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)

print(f"Model device: {model.device}")  # Should show 'mps:0'
print(f"Model dtype: {model.dtype}")    # Should show torch.float16

# LoRA config for efficient training
lora_config = LoraConfig(
    r=16,                    # Rank
    lora_alpha=32,           # Alpha
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
                   "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type=TaskType.CAUSAL_LM,
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# Debug: check gradient requirements
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Trainable parameters: {trainable_params}")

# Make sure model is in training mode
model.train()

print("Tokenizing datasets...")

def tokenize_batch(examples):
    texts = []
    for i in range(len(examples['input'])):
        text = examples['input'][i] + examples['target'][i] + tokenizer.eos_token
        texts.append(text)
    
    model_inputs = tokenizer(
        texts,
        max_length=256,
        truncation=True,
        padding="max_length",
        return_tensors="pt"
    )
    
    model_inputs["labels"] = model_inputs["input_ids"].clone()
    return {k: v.tolist() for k, v in model_inputs.items()}

train_dataset = train_dataset.map(
    tokenize_batch,
    batched=True,
    remove_columns=train_dataset.column_names
)

test_dataset = test_dataset.map(
    tokenize_batch,
    batched=True,
    remove_columns=test_dataset.column_names
)

# Data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,  # Causal LM, not masked LM
)

# Training arguments
training_args = TrainingArguments(
    output_dir="./gsm8k_step_by_step_model",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=4,
    warmup_steps=100,
    learning_rate=2e-4,
    logging_steps=50,
    eval_strategy="steps",
    eval_steps=200,
    save_steps=400,
    save_total_limit=2,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    report_to="wandb",
    dataloader_pin_memory=False,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset.select(range(100)),  # Small eval set
    data_collator=data_collator,
)

# Train
print("Starting training...")
trainer.train()

# Save the final model
print("Saving model...")
trainer.save_model("./gsm8k_final_model")
tokenizer.save_pretrained("./gsm8k_final_model")

print("Training complete!")