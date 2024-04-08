'''
Given a weighted directed acyclic graph (DAG) and two vertices - source and destination, 
find the least path cost from the source vertex to the destination vertex.

Scenario: Directed + acyclic + weighted + negative weights
This problem is suitable for a bellman-ford O(V*E) or dijsktra's 
We can do one pass of the bellman-ford if preprocess with topo sort 

'''

def least_path(edges:list[tuple], n:int, src:int, dest:int):
    adj = {k:[] for k in range(n)}
    for s,d,w in edges: 
        adj[s].append((d,w))

    visited = set()
    topo = []
    def dfs(adj, s):
        visited.add(s)
        for neighbor, _ in adj.get(s, []):
            if neighbor not in visited:
                dfs(adj,neighbor)
        topo.append(s)

    dfs(adj,src)
    topo = list(reversed(topo))

    # Bellman-ford
    distances = {k: float('inf') for k in range(n)}
    pred = {k: None for k in range(n)}
    distances[src] = 0

    def relax(u,v,w):
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
            pred[v] = u
    
    for v in topo:
        for u,w in adj.get(v, []):
            relax(v,u,w)
    
    return distances[dest]
    
edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)]
expected_output = 6
n = 8
src = 7
dest = 0

print(least_path(edges, n, src, dest))