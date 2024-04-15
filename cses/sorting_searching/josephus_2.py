# https://cses.fi/problemset/task/2162
import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
queue = deque(range(1,n+1))
ans=[]
while queue:
    queue.rotate(-(k))
    ans.append(queue.popleft())

print(' '.join(map(str,ans)))