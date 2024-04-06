'''
Given an undirected graph, check if it is a tree or not. 
In other words, check if a given undirected graph is an Acyclic Connected Graph or not.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)], n = 6]
Output: True
Explanation: Graph is connected and has no cycles.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], n = 6]
Output: False
Explanation: Graph contains cycle [0 —> 1 —> 2 —> 3 —> 4 —> 5 —> 0].

A tree is an undirected graph in which any two vertices are connected by exactly one path.
Any acyclic, connected graph is a tree 

'''

class Graph:
    def __init__(self,edges,n):
        self.adj = {k:[] for k in range(n)}
        for u,v in edges: 
            self.adj[u].append(v)
            self.adj[v].append(u)

def is_tree(edges,n):
    G = Graph(edges, n)
    visited = set()

    def dfs(v,parent):
        visited.add(v)
        for neighbor in G.adj.get(v):
            if neighbor not in visited:
                if not dfs(neighbor, v):
                    return False 
            elif neighbor != parent:
                return False 

        return True
    
    if not dfs(0,-1):
        return False
    
    return len(visited) == n 

edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5,0)]
n = 6

print(is_tree(edges,n))

