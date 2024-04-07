'''
Given an undirected graph, determine whether it is bipartite or not. A bipartite graph (or bigraph) is a graph whose vertices can be divided 
into two disjoint sets U and V such that every edge connects a vertex in U to one in V.

Input: Graph [edges = [(0, 1), (1, 2), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)], n = 9]
Output: True
Explanation: The graph is a bipartite as it can be divided it into two sets, U (0, 2, 4, 5, 7) and V (1, 3, 6, 8), with every edge having one endpoint in set U and the other in set V.

If we add edge 1 —> 3, the graph becomes non-bipartite.

Scenario:
- Undirected
- Unweighted
- Bipartiteness: Can you create two disjointed sets where every item of each set has a connection on the other

'''

class Graph:
    def __init__(self,edges,n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u,v in edges: 
            self.adj[u].append(v)
            self.adj[v].append(u)

def is_bipartite(graph):
    discovered = [False] * graph.n
    color = [False] * graph.n

    def dfs(u):
        discovered[u] = True
        for v in graph.adj[u]:
            if not discovered[v]:
                color[v] = not color[u]
                if not dfs(v):
                    return False
            elif color[v] == color[u]: # this is the critical check where you want alternate colors when for bipartiteness
                return False
        return True
    
    return dfs(0)

edges = [(0, 1), (1, 2), (1, 3), (1, 7), (2, 3), (3, 5), (4, 6), (4, 8), (7, 8)]
n = 9

print('is bipartite') if is_bipartite(Graph(edges, n)) else print('not bipartite') 
