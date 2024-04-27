# https://cses.fi/problemset/task/1070
import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())

def permute(arr, l, r):
    if l == r:
        prev = arr[0]
        for val in arr[1:]:
            if abs(val-prev)==1:
                return None
            prev = val
        return arr[:]
    
    for i in range(l,r):
        arr[i],arr[l]=arr[l],arr[i]
        result = permute(arr,l+1,r)
        if result is not None: 
            return result
        arr[i],arr[l]=arr[l],arr[i]

    return None 

nums = list(range(1,n+1))
ans=permute(nums,0,len(nums))
print(" ".join(map(str,ans)) if ans is not None else 'NO SOLUTION')