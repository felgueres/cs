# https://cses.fi/problemset/task/1643
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))

max_sub=arr[0]
cur=arr[0]
last = 0

for num in arr[1:]:
    if cur < 0 and num > 0:
        cur = num
    elif cur+num <0:
        max_sub=max(num, max_sub) 
        cur = 0
    elif cur+num >= 0: 
        cur+=num
        max_sub = max(cur,max_sub)

print(max_sub)