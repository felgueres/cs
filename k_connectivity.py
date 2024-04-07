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

Naive: Remove an edge and check if resulting graph is connected O(n^2)

When backtracking from a node v we need to ensure that 
there is a backedge from some descendant of v (including itself) to ancestor of v (parent or more).

https://www.techiedelight.com/2-edge-connectivity-graph/

'''
class Graph:
    def __init__(self,edges,n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u,v in edges:
            self.adj[u] = v
            # undirected
            self.adj[v] = u

def findBridges(graph:Graph):
    pass