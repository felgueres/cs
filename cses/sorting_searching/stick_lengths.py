# https://cses.fi/problemset/task/1074
# Finding min cost for stick lengths
# Get median, find abs distance to it for each element
import sys
n=int(sys.stdin.readline())
arr=sorted(list(map(int,sys.stdin.readline().strip().split()))) # n log n
mid=(len(arr))//2
min_stick = arr[mid]
print(sum([abs(a-min_stick) for a in arr]))