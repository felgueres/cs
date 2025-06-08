import warnings
warnings.filterwarnings("ignore", message=".*urllib3 v2 only supports OpenSSL.*")

from datasets import load_dataset
import re
import pandas as pd
from pathlib import Path

def prepare_gsm8k():
    """Load GSM8K, clean it, and save training data. One function, done."""
    gsm8k = load_dataset("gsm8k", "main")
    
    def clean_solution(text):
        lines = text.strip().split('\n')
        steps = []
        ans = None
        for line in lines:
            line = line.strip()
            if line.startswith('####'):
                ans = line.replace('####', '').strip()
            elif line:
                # Remove <<calc>> annotations and clean up
                cleaned = re.sub(r'<<[^>]+>>', '', line).strip()
                if cleaned:
                    steps.append(cleaned)
        return steps, ans

    data = {}
    for split in ['train', 'test']:
        examples = []
        for ex in gsm8k[split]:
            steps, answer = clean_solution(ex['answer'])
            if steps and answer:
                examples.append({
                    'problem': ex['question'],
                    'steps': steps,
                    'answer': answer,
                    'input': f"Problem: {ex['question']}\n\nSolution:\n",
                    'target': '\n'.join(steps)
                })
        data[split] = examples
    
    output_dir = Path(__file__).parent / "processed_gsm8k"
    output_dir.mkdir(exist_ok=True)
    
    for split, examples in data.items():
        pd.DataFrame(examples).to_csv(output_dir / f"{split}.csv", index=False)

    print(f"Train: {len(data['train'])}, Test: {len(data['test'])}")
    return data['train'], data['test']

if __name__ == "__main__":
    train, test = prepare_gsm8k()
    import pdb; pdb.set_trace()