# https://cses.fi/problemset/task/2183
# Min sum value you cannot create 
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split())) # n log n
# you need a counter and greedily increment
arr.sort()
# 1 2 2 7 9
smallest = 1
for num in arr:
    if num > smallest:
        break
    smallest+=num
print(smallest)