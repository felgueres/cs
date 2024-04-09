# https://cses.fi/problemset/task/1666
# Max recursion depth on some large cases but correct answer
import sys
sys.setrecursionlimit(10**6)
v,e = map(int,sys.stdin.readline().split())
edges = []
for i in range(e):
    s,d = map(int,sys.stdin.readline().split())
    edges.append((s,d))

adj={k:[] for k in range(1,v+1)}
for s,d in edges:
    adj[s].append(d)
    adj[d].append(s)

visited = set()

def dfs(root, path):
    visited.add(root)
    for neig in adj.get(root,[]):
        if neig not in visited:
            path.append(neig)
            dfs(neig, path)

components = []
for i in range(1,v+1):
    if i not in visited:
        path = [i]
        dfs(i,path)
        components.append(path)

new_roads = []
for i in range(1,len(components)):
    new_roads.append((components[i-1][0], components[i][0]))

print(len(new_roads))
for p,c in new_roads: print(f"{p} {c}")