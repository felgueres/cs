# https://cses.fi/problemset/task/1132 
# O(n^2) is not efficient, do two passes
                
import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline()) 

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().strip().split())
    adj[a].append(b)
    adj[b].append(a)

def find_longest(node):
    longest_dist = 0
    visited = [False]*(n+1)

    def dfs(node,dist=0):
        visited[node]=True
        nonlocal longest_dist
        if dist > longest_dist:
            longest_dist = dist
        for neig in adj[node]:
            if not visited[neig]:
                dfs(neig,dist+1)
    dfs(node)
    return longest_dist

for node in range(1,n+1): print(find_longest(node))
