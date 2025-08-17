import json
import pandas as pd
from config import BASE_DIR

# Load PRM800K data
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
    
    # Build complete solution by following the chosen path
    complete_solution_steps = []
    solution_is_correct = True  # Assume correct until we find a negative step
    
    for step_idx, step in enumerate(steps):
        if step['chosen_completion'] is not None:
            chosen_completion = step['completions'][step['chosen_completion']]
            chosen_text = chosen_completion['text']
            complete_solution_steps.append(chosen_text)
            
            # If any step in the chosen path is negative, solution is incorrect
            if chosen_completion.get('rating') == -1:
                solution_is_correct = False
                break  # Stop at first incorrect step
                
        elif step['human_completion'] is not None:
            complete_solution_steps.append(step['human_completion'])
    
    if complete_solution_steps:  # Only add if we have a complete solution
        complete_solution = '\n'.join(complete_solution_steps)
        input_text = f"Problem: {problem}\n\nSolution:\n{complete_solution}"
        
        # Binary classification: 0 = incorrect, 1 = correct
        label = 1 if solution_is_correct else 0
        
        formatted_data.append({
            'input_text': input_text,
            'label': label,
            'is_correct': solution_is_correct
        })

formatted_df = pd.DataFrame(formatted_data)
print(f"\nCorrectness distribution:")
print(formatted_df['is_correct'].value_counts())
print(f"\nLabel distribution:")
print(formatted_df['label'].value_counts())

print(f"\nFirst few examples:")
for i in range(min(3, len(formatted_df))):
    print(f"\nExample {i+1}:")
    print(f"Input: {formatted_df.iloc[i]['input_text'][:200]}...")
    print(f"Label: {formatted_df.iloc[i]['label']} ({'Correct' if formatted_df.iloc[i]['is_correct'] else 'Incorrect'})")

# Save the formatted data
output_path = BASE_DIR / "papers" / "01_lets_verify_step_by_step" / "data" / "prm800k"
output_path.mkdir(parents=True, exist_ok=True)
formatted_df.to_csv(output_path / "orm_train.csv", index=False)
print(f"\nSaved {len(formatted_df)} examples to orm_train_formatted.csv")
