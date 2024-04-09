# k shortest flight routes 
# route can visit city multiple times
# routes with same price and each should be considered
# directed, weighted, shortest with cycles
# stopped at 26mins
# This works but not fast enough wo cpp 

import sys
from heapq import heappush, heappop
from collections import defaultdict

n,m,k = map(int, sys.stdin.readline().split())

adj = defaultdict(list)
d = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    adj[a].append((c, b))

pq = []
heappush(pq, (0, 1))

while pq:
    cost, u= heappop(pq)
    if len(d[u]) >= k: 
        continue
    d[u].append(cost)
    for w, v in adj[u]:
        heappush(pq, (cost + w, v))

print(' '.join(map(str,d[n][:k])))