# https://cses.fi/problemset/task/1668
# Bipartiteness means there no cycle in a graph with 3 edges
# Fails on recursion depth but correct answer for small < 100K

import sys
sys.setrecursionlimit(10**6)
pupils,friendships = map(int,sys.stdin.readline().split())
adj = [[] for _ in range(pupils+1)]

for line in range(friendships):
    u,v = map(int,sys.stdin.readline().strip().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False]*(pupils+1)
color = [False]*(pupils+1)

def dfs(node):
    visited[node]=True 
    for neig in adj[node]:
        if not visited[neig]:
            color[neig] = not color[node] 
            if not dfs(neig):
                return False
        elif color[node] == color[neig]:
            return False
    return True

for i in range(1,pupils+1):
    if not visited[i]:
        if not dfs(i):
            print('IMPOSSIBLE')
            exit(0)

ans = []
for i in range(1,pupils+1):
    if color[i]:
        ans.append('2')
    else:
        ans.append('1')
print(' '.join(ans))