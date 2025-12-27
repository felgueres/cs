'''
This file follows Karpathy's lecture Let's build GPT: from scratch, spelled out 
https://www.youtube.com/watch?v=kCc8FmEb1nY&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&index=7

12/27/2025

Learnings:
- block_size is max length of context for prediction 
- batch_size is the number of independent sequences passed to GPUs, for efficiency
- negative_loss_likelihood is equivalent to cross_entropy in pytorch

'''

import torch

# input here is all the works from shakespeare downloaded from
# wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

with open('../data/input.txt', 'r') as f: text = f.read()
chars = sorted(list(set(text)))

stoi = { ch: i for i,ch in enumerate(chars)}
itos = { i: ch for i,ch in enumerate(chars)}

encode = lambda s: [stoi[c] for c in s] # outputs a list of integers
decode = lambda l: ''.join([itos[i] for i in l])

data = torch.tensor(encode(text), dtype=torch.long)

# let's make a split 90/10
n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]

# block_size is the maximum context length for predictions 
block_size = 8

x = train_data[:block_size]
y = train_data[1:block_size+1]


'''
for t in range(block_size):
    context = x[:t+1]
    target = y[t]
    print(f"when input is {context} the target: {target}")

This gives you an idea about the temporal dimension. 
We are making the transformer predict sequentially and may have as input from 1 to block_size
when input is tensor([18]) the target: 47
when input is tensor([18, 47]) the target: 56
when input is tensor([18, 47, 56]) the target: 57
when input is tensor([18, 47, 56, 57]) the target: 58
when input is tensor([18, 47, 56, 57, 58]) the target: 1
when input is tensor([18, 47, 56, 57, 58,  1]) the target: 15
when input is tensor([18, 47, 56, 57, 58,  1, 15]) the target: 47
when input is tensor([18, 47, 56, 57, 58,  1, 15, 47]) the target: 58
'''

# batch_size means how many independent sequences will we process in parallel
# batch_size is set to keep GPUs busy, it's for efficiency, not required
batch_size = 4

def get_batch(split="train"):
    # generate small batch of data of inputs x and targets y
    data = train_data if split == 'train' else val_data
    ix = torch.randint(len(data)-block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x,y

xb,yb = get_batch()
print(f"xb: {xb}\nyb:{yb}")

for b in range(batch_size): 
    for t in range(block_size):
        context = xb[b, :t+1]
        target = yb[b,t]
        print(f"when input is {context.tolist()} the target: {target}")

'''
Timestamp on video: 21:35

xb: tensor([[53, 53,  5, 42,  1, 51, 43,  1],
        [43, 56, 48, 59, 56, 43, 42,  1],
        [14, 30, 27, 23, 17, 10,  0, 30],
        [58, 46, 43,  1, 43, 42, 47, 41]])
yb:tensor([[53,  5, 42,  1, 51, 43,  1, 58],
        [56, 48, 59, 56, 43, 42,  1, 15],
        [30, 27, 23, 17, 10,  0, 30, 47],
        [46, 43,  1, 43, 42, 47, 41, 58]])
when input is [53] the target: 53
when input is [53, 53] the target: 5
when input is [53, 53, 5] the target: 42
when input is [53, 53, 5, 42] the target: 1
when input is [53, 53, 5, 42, 1] the target: 51
when input is [53, 53, 5, 42, 1, 51] the target: 43
when input is [53, 53, 5, 42, 1, 51, 43] the target: 1
when input is [53, 53, 5, 42, 1, 51, 43, 1] the target: 58
'''

# Until here, we have inputs and outputs to feed into the transformer 
# Let's start with a simple BigramModel

import torch.nn as nn
from torch.nn import functional as F
torch.manual_seed(1337)

class BigramLanguageModel(nn.Module):
    def __init__(self,vocab_size):
        super().__init__()
        # each token directly reads off the logits for the next token from a lookup table
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self,idx,targets):
        # idx and targets are both (B,T) tensor of integers
        # B = batch which is 4 (batch_size)
        # T = time which is 8 (block_size)
        # C = channels which is vocab_size
        logits = self.token_embedding_table(idx) # (B,T,C)
        B,T,C = logits.shape
        logits = logits.view(B*T, C) # this is just reshaping to conform w pytorch api
        targets = targets.view(B*T)
        loss = F.cross_entropy(logits,targets) # measures quality of predictions vs. targets
        return logits, loss

    def generate(self,idx,max_new_tokens):
        # idx is (B,T) array of indices in the current context
        for _ in range(max_new_tokens):
            # get predictions
            logits, loss = self(idx) # this calls forward with a few hooks to track gradients
            # focus only on the last time step
            logits = logits[:, -1, :] # becomes (B,C)
            # apply softmax to get probabilities
            probs=F.softmax(logits, dim=1) # (B,C)
            # sample from the distribution 
            idx_next = torch.multinomial(probs,num_samples=1) # (B,1)
            # append sampled index to the running sequence
            idx = torch.cat((idx,idx_next), dim=1) # (B,T+1)

vocab_size = 65
m = BigramLanguageModel(vocab_size)
logits, loss = m(xb,yb)
print(loss)

