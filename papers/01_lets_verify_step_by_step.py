'''
Let's verify step-by-step (5/2023)
https://arxiv.org/pdf/2305.20050

Why it matters? 
- Step-by-step feedback creates better reasoning judges

What exactly did they do?
- Train a generator model 
- Generate labels to train an outcome reward model and a process reward model
- PRM is trained to output positive/negative/neutral. So if you get the softmax(logits), you can get the probability of correctness
- Generate 1870 exmaples of math questions
- ORM scoring: looks at final token and predicts probability of correctness
- PRM scoring: looks at each step and predicts probability. The solution score is the product of probabilities for all steps.
- Sort ranked solutions, pick highest, check if it's correct

Sota models still produce logical mistakes.
1) improve outcome supervision, or, 2) process supervision
difference being the stage at which you capture feedback, 
either at final result or throughout reasoning steps
Findings: 
- process significantly outperforms outcome supervision on MATH dataset
- active learning improves efficacy of process supervision

Training dataset: PRM800K 
- 800K step-level human feedback labels to train best reward model
- https://github.com/openai/prm800k

An effective method to mitigate halucination is to train a reward model to 
discriminate between desirable and undesirable outputs.

This reward model can then be used:
- In a reinforcement learning pipeline. Use model as critic to score model quality output, 
  then maximize score using Proximal Policy Optimization to shift the model behavior towards 
  reward model preferences. This is RL and modifies model weights.
- Or to perform search via rejection sampling. Just sample the model, 
  score with reward model, and pick highest. Doesn't affect weights.

To train reward models, 2 methods: 
- Outcome-supervised reward models (ORMs). Trained using final result of the chain of thought.
- Process-supervised reward models (PRMs). Receive feedback for each step of the chain of thought.

Scope
- Single fixed model to generate all solutions, this is the generator model
- Outcome and Process in this paper refers to the supervision given to the reward model 
- Note that you could imporve the generator model using the reward model but that's not discussed here.
- The focus here is on training a reliable reward model
- Eval on the reward model is its ability to perform best-of-N search over uniformly sampled solutions from the generator

Eval
- Generate 1860 solutions per math problem using a generator
- Had each evaluator rank all 1860 solutions
- Pick the top-ranked solution and checked if it got the right final answer
- PRM picked good solutions 78.2% of the time, ORM 72.4%

ORM training:
Solution 1: [steps...] → Final answer: 42 → Label: CORRECT
Solution 2: [steps...] → Final answer: 37 → Label: WRONG

PRM training:
Solution: 
Step 1: "Set up equation" → POSITIVE
Step 2: "Subtract 5 from both sides" → POSITIVE  
Step 3: "So x = 12" → NEGATIVE (this step was wrong)
Step 4: [solution stops here - they only label up to first mistake]

Generator model
- 200X less compute than GPT4 + pretraining step oof 1.5B math-relevant tokens
- To make the output easier to parse, they few shot the generator to produce solutions with newline delimited step-by-step format

Data collection
- Present humans with step-by-step solutions to math problems sampled from the large-scale generator
- Human labeler assigns each step a label of positive, negative, or neutrals
- reasoning_step, label

Active learning
- Train PRM_selector model on a single sample from each problem
- Use this model to score 1K samples per problem
- To train each of the larger reward models:
- - select N samples per problem such that 80% are the most convincing wrong-answer samples according to PRM_selector
- - 20% are the most convincing samples that remain (right-or wrong-answer) 
- Score  selected samples with PRM_large and train on those scores
- This helps all samples be relatively convicning under PRM_selector and that a large fraction contain at least one mistake
- Comparing the slopes best fit lines with and without active learning, active learning is 2.6X more data efficient than uniform data labelling

Conclusion
- Process-supervised learning produces more reliable reward models than outcome-based
- Active learning helps lower the cost of human data collection by sampling most valuable examples 
- PRM is a negative "tax" for alignment (better) since gives you ability to provide continuous feedback  
- Best of N means sample a lot of solutions and score them with a reward model. Return the one that does the best
- With a good enough reward model, BoN (best of N) beats consensus (generate bunch of answers pick the most common)
- BoN is ultimately bottlenecked by a reward model

How to do research?
- Planning is a good domain for academic research. Because large companies prefer high upfront costs and low inference costs, so their incentives are there. 
- You only need a few examples to prove out an idea
- What's critical is to have a good external verifier so you're not being bottlenecked by reward model quality

Follow ups 
1. X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, and D. Zhou. Self-consistency
improves chain of thought reasoning in language models. 
  Why it matters? 
    - Shows importance of explicitly performing intermediate reasoning steps via chain of though or a scratchpad  to solve multi-step reasoning. 

2. T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa. Large language
models are zero-shot reasoners. 
  Why it matters? 
    - Shows that models can do this zero-shot conditioned only on a simple prompt.
repro: https://huggingface.co/meta-llama/Llama-3.2-1B

'''
