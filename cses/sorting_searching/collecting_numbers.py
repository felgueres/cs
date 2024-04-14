# https://cses.fi/problemset/task/2216
# arr contains 1 ... n exactly once
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))

num_dict={}

for i,x in enumerate(arr): # O(n)
    num_dict[x] = i

rounds=1
cur=0

for i in range(1,n+1):
    if num_dict[i]<cur:
        rounds+=1
    cur = num_dict[i]

print(rounds)