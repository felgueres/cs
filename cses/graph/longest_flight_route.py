# https://cses.fi/problemset/task/1680
# has mistakes

import sys
sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,sys.stdin.readline().strip().split())
    adj[u].append(v)

src = 1  
dest = n
visited = set()
longest_path = [] 

def dfs(current,path):
    global longest_path
    visited.add(current)

    if current == n:
        if len(path) > len(longest_path):
            longest_path = path.copy()
        return

    for neig in adj[current]:
        if neig not in visited:
            dfs(neig,path+[neig])

    visited.remove(current)

dfs(1, [1])

if len(longest_path) == 0:
    print("IMPOSSIBLE")
else:
    print(len(longest_path))
    print(' '.join(map(str,longest_path)))