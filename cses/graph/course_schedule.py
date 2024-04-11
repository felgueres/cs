# https://cses.fi/problemset/task/1679

import sys
sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())

adj=[[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int,sys.stdin.readline().strip().split())
    adj[u].append(v)

visited = [0] * (n+1)
sorted_dag = []
def topo(v):
    if visited[v] == 1:  # Cycle detected
        print("IMPOSSIBLE")
        sys.exit(0)
    if visited[v] == 0:
        visited[v] = 1  # Mark as visiting
        for neig in adj[v]:
            topo(neig)
        visited[v] = 2  # Mark as visited
        sorted_dag.append(v)


for v in range(1,n+1):
    if visited[v]==0:
        topo(v)

print(' '.join(map(str,reversed(sorted_dag))))