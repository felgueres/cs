import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification, 
    TrainingArguments, 
    Trainer,
    DataCollatorWithPadding
)
from peft import LoraConfig, get_peft_model, TaskType
import pandas as pd
from datasets import Dataset
import wandb
import numpy as np
from sklearn.metrics import accuracy_score
from config import BASE_DIR

import warnings
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL.*")

# Initialize wandb
wandb.init(
    project="prm-step-verification",
    name="gemma-2b-prm-lora",
    config={
        "model": "google/gemma-2b",
        "lora_rank": 16,
        "lora_alpha": 32,
        "learning_rate": 1e-5,
        "batch_size": 8,
        "effective_batch_size": 128,
        "epochs": 2,
        "num_labels": 3
    }
)

print("Loading PRM data...")
train_df = pd.read_csv(BASE_DIR / "papers" / "01_lets_verify_step_by_step" / "data" / "prm800k" / "phase2_train.csv")

# Reduce sample size even further for OOM issues
SAMPLE_SIZE = 50000  # Reduced from 2000
if len(train_df) > SAMPLE_SIZE:
    train_df = train_df.sample(n=SAMPLE_SIZE, random_state=42)
    print(f"Sampled down to {SAMPLE_SIZE} examples")

train_dataset = Dataset.from_pandas(train_df)
print(f"Train examples: {len(train_dataset)}")

# Load tokenizer and model for classification
print("Loading Gemma-2B for classification with LoRA...")
model_name = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=3,  # 3 classes: 0, 1, 2 (for ratings -1, 0, +1)
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True,
    use_cache=False  # Disable KV cache to save memory
)

print(f"Model device: {model.device}")
print(f"Model dtype: {model.dtype}")

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
                   "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type=TaskType.SEQ_CLS,  # Sequence Classification
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# Ensure LoRA parameters are in float32 for gradient computation
for param in model.parameters():
    if param.requires_grad:
        param.data = param.data.float()

trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"Trainable parameters: {trainable_params}")

model.train()

print("Tokenizing datasets...")

def tokenize_batch(examples):
    model_inputs = tokenizer(
        examples['input_text'],
        max_length=512,  # Reduced from 1024
        truncation=True,
        padding=True,  # Dynamic padding instead of max_length
        return_tensors="pt"
    )
    
    model_inputs["labels"] = examples["label"]
    return {k: v.tolist() if isinstance(v, torch.Tensor) else v for k, v in model_inputs.items()}

train_dataset = train_dataset.map(
    tokenize_batch,
    batched=True,
    remove_columns=train_dataset.column_names
)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return {"accuracy": accuracy_score(labels, predictions)}

training_args = TrainingArguments(
    output_dir="./prm_model",
    num_train_epochs=2,  # Reduced from 2
    per_device_train_batch_size=2,  # Reduced from 8
    per_device_eval_batch_size=2,  # Reduced from 8
    gradient_accumulation_steps=32,  # Increased to maintain effective batch size
    warmup_steps=100,  # Reduced from 100
    learning_rate=1e-5,
    logging_steps=100,  # Reduced from 100
    eval_strategy="steps",
    eval_steps=500,  # Reduced from 500
    save_steps=1000,  # Reduced from 1000
    save_total_limit=1,  # Reduced from 2
    load_best_model_at_end=False,  # Disable to save memory
    metric_for_best_model="accuracy",
    greater_is_better=True,
    report_to="wandb",
    dataloader_pin_memory=False,
    bf16=True,  # Use bf16 instead of fp16 for better stability
    gradient_checkpointing=True,  # Trade compute for memory
    dataloader_num_workers=0,  # Reduce CPU memory usage
    remove_unused_columns=False,  # Keep all columns for debugging
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=train_dataset.select(range(2000)),  # Much smaller eval set
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

print("Starting PRM training...")
trainer.train()

print("Saving PRM model...")
trainer.save_model("./prm_final_model")
tokenizer.save_pretrained("./prm_final_model")