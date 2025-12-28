'''
This file follows Karpathy's lecture Let's build GPT: from scratch, spelled out 
https://www.youtube.com/watch?v=kCc8FmEb1nY&list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&index=7

12/27/2025

Learnings:
- [Attention Is All You Need](https://arxiv.org/pdf/1706.03762): We're implementing the decoder-only part of this paper. The left-side is the encoder which is used in machine translation and connects to this transformer using cross-attention.
- block_size is max length of context for prediction 
- batch_size is the number of independent sequences passed to GPUs, for efficiency
- negative_loss_likelihood is equivalent to cross_entropy in pytorch
- self-attention relies on a matmul trick which is to multiply a bottom-triangular matrix of ones (bottom) and zeros (top). After softmaxing that matrix with masking zeros with -inf, you get cumulative weights that basically lets tokens share information with the past, not the future. Basically, you can do weigthed agg of past elements by using matmul of a lower triangular fashion, and then elements in the lower triangular part are telling you how much of the element fuses into a position. 
- [Dropout](https://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf?utm_content=buffer79b4) is a technique to prevent overfitting, which is to disable a percentage of neurons during training, and then reenabling at test time. 
- The original transformer paper is decoder/encoder transformer. You can train a decoder only transformer which is what's below. When you add the encoder block you can also do cross attention between the decoder-only blocks and it. The thing that makes it a decoder is the fact that we are using the triangular mask 
- Autoregressive means that each token representation is computed using past and current tokens only, never future ones, which is introduced by the causal mask (bottom triangular mask)
- Heads are attention heads, where a heaad is one independent self-attention operation with its own Q,K,V projection. During training there are emerging properties they might specialize on but they're not controllable, or assigned, any specialization is emergent and soft. However there are ways to bias or constrain heads by applying different masks per head.
- Good questions to ask on over sellers: 1) can the specialization be ablated? 2) Are heads hard-constraineed or probed after training? Do you enforce the heads via masking?
- Q, K, V are Query, Key, Value matrices. People attach names and ideas but concretely they derive their meaning from math semantics as used in the equation, so:
weights = softmax(Q Kᵀ)
output  = weights V
Q is the thing that queries via a dot product
K is the thing being queried against
V is the thing whose contents get returned

Input Tensor Shape: [ batch_size , block_size ]
Input Tensor Shape: [ batch_size , block_size ]

batch_size = number of sequences processed in parallel
block_size = number of tokens (time steps) per sequence

                    ┌───────────────────────────────────┐
Sequence 1 (sample) │ t1   t2   t3   t4   ...   tN      │
                    ├───────────────────────────────────┤
Sequence 2 (sample) │ t1   t2   t3   t4   ...   tN      │
                    ├───────────────────────────────────┤
Sequence 3 (sample) │ t1   t2   t3   t4   ...   tN      │
                    ├───────────────────────────────────┤
        ...         │ ...  ...  ...  ...  ...  ...      │
                    ├───────────────────────────────────┤
Sequence B (sample) │ t1   t2   t3   t4   ...   tN      │
                    └───────────────────────────────────┘
                         ↑                       ↑
                         └─── block_size (N) ────┘
        ↑
        └──────────── batch_size (B) ─────────────┘
'''

import torch
torch.manual_seed(42)

# input here is all the works from shakespeare downloaded from
# wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

with open('./data/input.txt', 'r') as f: text = f.read()
chars = sorted(list(set(text)))
vocab_size = len(chars) 

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

'''
Timestamp on video: 21:35

print(f"xb: {xb}\nyb:{yb}")

for b in range(batch_size): 
    for t in range(block_size):
        context = xb[b, :t+1]
        target = yb[b,t]
        print(f"when input is {context.tolist()} the target: {target}")

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

    def forward(self,idx,targets=None):
        logits = self.token_embedding_table(idx) # (B,T,C)
        # idx and targets are both (B,T) tensor of integers
        # B = batch which is 4 (batch_size)
        # T = time which is 8 (block_size)
        # C = channels which is vocab_size
        if targets == None:
            loss = None
        else:
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
            # focus only on the last time step (plucks out the last in the time dimension)
            logits = logits[:, -1, :] # becomes (B,C)
            # apply softmax to get probabilities
            probs=F.softmax(logits, dim=1) # (B,C)
            # sample from the distribution 
            idx_next = torch.multinomial(probs,num_samples=1) # (B,1)
            # append sampled index to the running sequence
            idx = torch.cat((idx,idx_next), dim=1) # (B,T+1)
        return idx


"""
m = BigramLanguageModel(vocab_size)
logits, loss = m(xb,yb)
print(logits.shape)
print(loss)
# Predicting and concatenating outputs to create sequence
print(decode(m.generate(torch.zeros((1,1), dtype=torch.long), max_new_tokens=100)[0].tolist()))
$ SKIcLT;AcELMoTbvZv C?nq-QE33:CJqkOKH-q;:la!oiywkHjgChzbQ?u!3bLIgwevmyFJGUGp wnYWmnxKWWev-tDqXErVKLgJ
GIBERRISH! That's because we haven't trained the model but we go from single token to concatenating max_new_tokens!
"""

# Now we actually need to train model
# A typical learning rate (lr) is 3e-4 but for smaller nn like this one, bigger number is ok

batch_size = 32
first_step = True
eval_iters = 10_000 
learning_rate = 1e-3

"""
optimizer = torch.optim.AdamW(m.parameters(), lr=1e-3)
for steps in range(eval_iters):
    # sample a batch of data
    xb,yb = get_batch('train')
    # evaluate the loss
    logits, loss = m(xb,yb)
    if first_step: 
        print(f"Init loss: {loss.item():.2f}")
        first_step=False
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    # print here all loss.item() to see the improvement!

print(f"Loss after {eval_iters} eval_iters: {loss.item():.2f}")
print(f"GENERATED OUTPUT")
print(decode(m.generate(torch.zeros((1,1), dtype=torch.long), max_new_tokens=300)[0].tolist()))

OUTPUT 
------

LA c wo the;
Pancalolinghowhatharean:
QA:

Wwhass bowoond;
Fomere d shdeenotep.
CI y mbotot swefesealso br. ave aviasurf my, yxMPZI ivee iuedrd whar ksth y h bora s be hese, woweee; the! KI 'de, ulseecherd d o blllando;LUCEO, oraingofof win!
RIfans picspeserer hee anf,
TOFonk? me ain ckntoty dedo bo

# MUCH BETTER BUT IT AINT SHAKESPEARE YET
# This model is very simple and tokens are not talking to each other, it's simply predicting next token T+1 using T only
# Video TS to resume: https://youtu.be/kCc8FmEb1nY?si=qQmXZXDp1NRIAdxR&t=2275
"""

# hyperparams
batch_size = 32 # number of independent sequecnes to process in parallel
block_size = 8 # maximum context length for prediction
max_iters = 3000
eval_interval=300
learning_rate = 1e-2
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
# ---------------


torch.manual_seed(1337)

model = BigramLanguageModel(vocab_size)
m = model.to(device)
optimizer = torch.optim.AdamW(model.parameters(),lr=learning_rate)

@torch.no_grad()
def estimate_loss():
    out = {}
    model.eval()
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            X,Y = get_batch(split)
            logits, loss = model(X,Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    model.train()
    return out

for iter in range(max_iters):
    # every once in a while evaluate the loss on train and eval sets
    if iter % eval_interval == 0:
        losses = estimate_loss()
        print(f"step {iter}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

    # sample data
    xb,yb = get_batch('train')
    # evaluate loss
    logits,loss = model(xb,yb)
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()

context = torch.zeros((1,1), dtype=torch.long, device=device)
print(decode(m.generate(torch.zeros((1,1), dtype=torch.long), max_new_tokens=300)[0].tolist()))

