'''
Given an undirected connected graph, return a set of all bridges in the graph. 
A bridge is an edge of a graph whose removal disconnects the graph.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3)], n = 4]
Output: {(0, 1), (1, 2), (2, 3)}
Explanation: The graph has 3 bridges {(0, 1), (1, 2), (2, 3)}, since removal of any of it disconnects the graph.

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 0)], n = 4]
Output: {}
Explanation: The graph is 2–edge connected. i.e., it remains connected on removal of any edge.

Note: 
The solution should return edges in increasing order of node's value. 
For instance, both (1, 2) and (2, 1) represent the same edge in an undirected graph. 
The solution should return edge (1, 2).

Naive: Remove an edge and check if resulting graph is connected O(E * (V+E))

An edge (v,to) is a bridge iff none of the vertices `to` and its descendants in the DFS tree has a back-edge to vertex v or any ancestor.
Meaning that there's no way from `v` to `to` except for edge (v,to)

Ultimately you want to check that low[to] > tin[v] = 'is_bridge'

'''
class Graph:
    def __init__(self,edges,n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u,v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)

def findBridges(graph:Graph):
    global visited, tin, low, timer
    timer = 0
    visited = [False] * graph.n
    tin = [-1] * graph.n
    low = [-1] * graph.n # lowest visit time for all nodes reachable from a node

    def dfs(v,p):
        global timer
        visited[v] = True
        timer += 1
        tin[v] = low[v] = timer # initalia discovery time and low value
        for to in graph.adj[v]:
            if to == p: # if adj node is the parent, skip it
                continue
            if visited[to] and to!=p: # node already visited, this is a backedge
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, v)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    print(f"Bridge found between nodes {v} and {to}")

    for i in range(graph.n):
        if not visited[i]:
            dfs(i,-1)

edges = [(0, 1), (1, 2), (2, 3)] 
print(findBridges(Graph(edges,len(edges)+1)))