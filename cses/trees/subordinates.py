# https://cses.fi/problemset/task/1674
# subordinates problem
# this problem can be solved by counting the the number of nodes for each node subtree

import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
db_arr = map(int,sys.stdin.readline().strip().split())
edges = list(zip(db_arr,[e for e in range(2,n+1)]))
adj = [[] for _ in range(n+1)]
for (u,v) in edges:
    adj[u].append(v)

count = [0]*(n+1)
def dfs(s):
    count[s] = 1 # counts itself, line 27 adjusts for it 
    for u in adj[s]:
        dfs(u)
        count[s] += count[u]

dfs(1)

for i in range(1,n+1):
    count[i] -= 1

print(" ".join(map(str,count[1:])))