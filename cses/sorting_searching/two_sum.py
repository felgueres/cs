# https://cses.fi/problemset/task/1640
import sys
n,x=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().strip().split()))
vals = {}
for i in range(len(arr)):
    if arr[i] in vals:
        print(f"{vals[arr[i]]+1} {i+1}")
        exit(0)
    vals[x-arr[i]] = i

print('IMPOSSIBLE')