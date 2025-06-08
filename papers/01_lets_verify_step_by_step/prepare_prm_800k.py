import json
import pandas as pd
from config import BASE_DIR

prm800k_path = BASE_DIR / "papers" / "01_lets_verify_step_by_step" / "data/prm800k/source" 
data_files = list(prm800k_path.glob("phase2_train.jsonl"))
examples = []

with open(data_files[0], 'r') as f:
    for line in f:
        examples.append(json.loads(line))

formatted_data = []

for example in examples:
    problem = example['question']['problem']
    steps = example['label']['steps']
    cumulative_steps = []
    for step_idx, step in enumerate(steps):
        for completion in step['completions']:
            if completion['rating'] is None:
                continue
            current_step = completion['text']
            if cumulative_steps:
                partial_solution = '\n'.join(cumulative_steps) + '\n' + current_step
            else:
                partial_solution = current_step
            input_text = f"Problem: {problem}\n\nSolution so far:\n{partial_solution}"
            rating_to_label = {-1: 0, 0: 1, 1: 2}  # Convert to 0,1,2 for classification
            label = rating_to_label[completion['rating']]
            formatted_data.append({
                'input_text': input_text,
                'label': label,
                'rating': completion['rating']  # Keep original for reference
            })
        if step['chosen_completion'] is not None:
            chosen_text = step['completions'][step['chosen_completion']]['text']
            cumulative_steps.append(chosen_text)
        elif step['human_completion'] is not None:
            cumulative_steps.append(step['human_completion'])

formatted_df = pd.DataFrame(formatted_data)
print(f"\nRating distribution:")
print(formatted_df['rating'].value_counts())
print(f"\nLabel distribution:")
print(formatted_df['label'].value_counts())

print(f"Examples:")
for i in range(min(3, len(formatted_df))):
    print(f"\nExample {i+1}:")
    print(f"Input: {formatted_df.iloc[i]['input_text'][:200]}...")
    print(f"Label: {formatted_df.iloc[i]['label']}")

formatted_df.to_csv(BASE_DIR / "papers" / "01_lets_verify_step_by_step" / "prm800k" / "phase2_train_formatted.csv", index=False)