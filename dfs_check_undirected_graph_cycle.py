# Given an undirected graph, determine whether it contains any cycle.

# Input: Graph [edges = [(0, 1), (1, 2), (0, 2)], n = 3]
# Output: True

# Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (1, 4)], n = 5]
# Output: False

# edges = [(0, 1), (1, 2), (0, 2)]
# n = 3 

# 0 -> 1: parent for 1 is 0
# 1 -> 2: parent for 2 is 1
# 0 -> 2: parent for 2 is 0

# 2 has two parents, this means a cycle

edges = [(0, 1), (1, 2), (2, 3), (1, 4)]
n=5

def traversal(edges,n):
    visited = [False]*n
    adj = {k:[] for k in range(n)}
    ancestors = {k: None for k in range(n)}

    for (u,v) in edges: 
        adj[u].append(v)
        adj[v].append(u)

    def dfs(node):
        visited[node] = True
        for neighbor in adj.get(node,[]):
            if not visited[neighbor]:
                ancestors[neighbor] = node
                dfs(neighbor)
        
    for v in range(n):
        if not visited[v]:
            dfs(v)
    
    return ancestors
