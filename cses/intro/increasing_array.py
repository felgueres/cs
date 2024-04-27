# https://cses.fi/problemset/task/1094

import sys
n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().strip().split()))

cur = array[0]
steps = 0 
for num in array[1:]: 
    if num < cur:
        steps+=(cur-num)
        continue
    cur = num

print(steps)