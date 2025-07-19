'''Least cost path in a digraph from a given source to a destination having exactly `m` edges
Given a weighted digraph (directed graph), find the least-cost path from a given source to a given destination with exactly m edges.

Intuition:
- This problem has 2 constraints, least-cost path and exact edge count. 
- Vanilla BFS gets you shortest path, but here we need to relax it to explore all paths
- When exploring, we'll keep the depth of the BFS to be <= `m`
- By having that check you can't get into an indefinite cycle loop 

'''
# A - B - C - D (m+1)

# First, lets build the adj list
from collections import deque

def least_cost(edges,n,src,dest,m):
    adj = {k:[] for k in range(n)}
    for u,v,d in edges: 
        adj[u].append((v,d))

    queue = deque([(src,0,[src],0)])
    # target depth = m+1
    paths = []

    while queue:
        s, depth, path, cost = queue.popleft()
        print(f"s: {s} depth: {depth} cost: {cost}")

        if depth == m and s == dest:
            paths.append((path, cost))

        if depth < m:
            print(f'scanning: {s}')
            for neighbor,w in adj.get(s, []):
                print(f"visiting neighbord: {neighbor}")
                queue.append((neighbor,depth+1,path+[neighbor], cost+w))
        
        if depth > m:
            break

    return paths 

edges = [ (0, 6, -1), (0, 1, 5), (1, 6, 3), (1, 5, 5), (1, 2, 7), (2, 3, 8), (3, 4, 10), (5, 2, -1), (5, 3, 9), (5, 4, 1), (6, 5, 2), (7, 6, 9), (7, 1, 6) ]
n = 8
src = 0
dest = 3
m = 4

print(least_cost(edges,n,src,dest,m))