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
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from config import BASE_DIR

import warnings
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL.*")

# Initialize wandb
wandb.init(
    project="orm-outcome-verification", 
    name="gemma-2b-orm-lora",
    config={
        "model": "google/gemma-2b",
        "lora_rank": 16,
        "lora_alpha": 32,
        "learning_rate": 1e-5,
        "batch_size": 2,
        "effective_batch_size": 64,
        "epochs": 2,
        "num_labels": 2  # Binary classification: correct/incorrect
    }
)

print("Loading ORM data...")
train_df = pd.read_csv(BASE_DIR / "papers" / "01_lets_verify_step_by_step" / "data" / "prm800k" / "orm_train.csv")

# Reduce sample size for memory management
SAMPLE_SIZE = 1000
if len(train_df) > SAMPLE_SIZE:
    train_df = train_df.sample(n=SAMPLE_SIZE, random_state=42)
    print(f"Sampled down to {SAMPLE_SIZE} examples")

train_dataset = Dataset.from_pandas(train_df)
print(f"Train examples: {len(train_dataset)}")
print(f"Label distribution: {train_df['label'].value_counts().to_dict()}")

# Load tokenizer and model for binary classification
print("Loading Gemma-2B for binary classification with LoRA...")
model_name = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=2,  # Binary: incorrect (0) vs correct (1)
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True,
    use_cache=False
)

print(f"Model device: {model.device}")
print(f"Model dtype: {model.dtype}")

# LoRA configuration for ORM
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
                   "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type=TaskType.SEQ_CLS,
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
        max_length=512,
        truncation=True,
        padding=True,
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
    
    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='binary')
    
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

training_args = TrainingArguments(
    output_dir="./orm_model",
    num_train_epochs=2,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=16,  # Effective batch size = 2 * 16 = 32
    warmup_steps=100,
    learning_rate=1e-5,
    logging_steps=100,
    eval_strategy="steps",
    eval_steps=500,
    save_steps=1000,
    save_total_limit=1,
    load_best_model_at_end=False,
    metric_for_best_model="f1",
    greater_is_better=True,
    report_to="wandb",
    dataloader_pin_memory=False,
    bf16=True,
    gradient_checkpointing=True,
    dataloader_num_workers=0,
    remove_unused_columns=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=train_dataset.select(range(2000)),  # Small eval set
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

print("Starting ORM training...")
trainer.train()

print("Saving ORM model...")
trainer.save_model("./orm_final_model")
tokenizer.save_pretrained("./orm_final_model")