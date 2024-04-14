# https://cses.fi/problemset/task/1141
# sliding window technique
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))
# successive uniques
last_seen={}
max_unique=0
start=0
for i,num in enumerate(arr):
    if num in last_seen and last_seen[num]>=start:
        start=last_seen[num]+1
    last_seen[num]=i
    max_unique=max(max_unique,i-start+1)
print(max_unique)