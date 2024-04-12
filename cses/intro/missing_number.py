import sys
n = int(sys.stdin.readline())
nums = map(int,sys.stdin.readline().strip().split())
# 1 2 3 (4 missing)
# 1 3 6 10
# function that sums 

def cumsum(n): return n * (n+1)//2

print(cumsum(n)-sum(nums))