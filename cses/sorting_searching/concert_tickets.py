# https://cses.fi/problemset/task/1091/
# classical binary search + fuzzyness

import sys

n,m=map(int,sys.stdin.readline().split())
prices=sorted(list(map(int,sys.stdin.readline().strip().split())))
maxp=list(map(int,sys.stdin.readline().strip().split()))

def bs(prices,target):

    if len(prices) == 0:
        return -1,[]

    if len(prices) == 1 and prices[0]<=target:
       ans = prices[0] 
       prices.pop(0)
       return ans,prices

    low = 0
    high = len(prices)-1

    while low < high:
        mid = (low+high)//2
        if target <= prices[mid]:
            high = mid
        else: 
            low = mid+1 
    if 0<=high<len(prices) and target == prices[high]:
        ans = prices[high]
        prices.pop(high)
        return ans,prices 

    elif 0 <= high-1 and prices[high-1] <= target:
        ans = prices[high-1]
        prices.pop(high-1) 
        return ans,prices 

    else:
        return -1,prices 

for p in maxp: 
    ans,prices = bs(prices,p)
    print(ans)
