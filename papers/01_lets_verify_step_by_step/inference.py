import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from config import BASE_DIR
import tarfile

cur_dir = BASE_DIR / 'papers' / '01_lets_verify_step_by_step'

with tarfile.open(cur_dir / 'gsm8k_final_model.tar.gz', 'r:gz') as tar:
    tar.extractall(cur_dir)

print("Loading base model...")
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b",
    torch_dtype=torch.float16,
    device_map="auto",
    low_cpu_mem_usage=True
)

print("Loading trained LoRA adapters...")
model = PeftModel.from_pretrained(model, cur_dir / "gsm8k_final_model")

print("Testing trained model...")

# Test with a GSM8K-style problem
prompt = """Problem: Janet has 16 apples. She eats 3 and gives 5 to her friend. How many apples does she have left?

Solution:
"""

inputs = tokenizer(prompt, return_tensors="pt")
inputs = {k: v.to(model.device) for k, v in inputs.items()}

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=300,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

result = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("=== TRAINED MODEL OUTPUT ===")
print(result)
print("=" * 50)
