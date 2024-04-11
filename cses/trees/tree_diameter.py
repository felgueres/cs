# https://cses.fi/problemset/task/1131
# Good solution, needs cpp to pass time limits 
                
import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline()) 
if n == 1:
    print(0)
    exit(0)

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().strip().split())
    adj[a].append(b)
    adj[b].append(a)

def find_longest(node):
    longest_node = None 
    longest_dist = 0
    visited = [False]*(n+1)

    def dfs(node,dist=0):
        visited[node]=True
        nonlocal longest_node,longest_dist
        if dist > longest_dist:
            longest_node = node 
            longest_dist = dist
        for neig in adj[node]:
            if not visited[neig]:
                dfs(neig,dist+1)
    dfs(node)
    return longest_node, longest_dist

u,dist_u = find_longest(1) # this will always take you to one of the endpoints of the diameter
v,ans= find_longest(u)
print(ans)
