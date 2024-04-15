# https://cses.fi/problemset/task/2162
import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque(range(1,n+1))
ans=[]
while queue:
    # first=queue.pop(0)
    # queue.append(first)
    # second=queue.pop(0) 
    # ans.append(second)
    # pop from the left and add to the right can be done with deque.rotate(-1) 
    queue.rotate(-1)
    ans.append(queue.popleft())

print(' '.join(map(str,ans)))