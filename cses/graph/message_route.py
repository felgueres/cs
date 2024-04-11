# https://cses.fi/problemset/task/1667
import sys 
from collections import deque
n,m = map(int,sys.stdin.readline().split())
edges = []
for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    edges.append((u,v))

adj = [[] for _ in range(n+1)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

src = 1
dest = n

queue = deque([(src, [src])])
visited = set()

found = False
while queue and not found:
    node,path = queue.popleft()
    for neig in adj[node]:
        if neig == dest:
            npath = path+[neig]
            print(len(npath))
            print(' '.join(map(str, npath)))
            found = True
            break

        if neig not in visited:
            visited.add(neig)
            queue.append((neig, path+[neig]))

if not found:
    print('IMPOSSIBLE')