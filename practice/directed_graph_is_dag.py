'''

Given a directed graph, check if it is a DAG (Directed Acyclic Graph) or not. 
A DAG is a digraph (directed graph) that contains no cycles.

Input: Graph [edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)], n = 7]
Output: False
Explanation: The graph contains a cycle [0 -> 1 -> 3 -> 0].

If we remove edge [3 -> 0] from it, it will become a DAG.

Input: Graph [edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (5, 6), (6, 3)], n = 7]
Output: True

Back edge
    Connects a vertex to an ancestor in the dfs tree, this creates a cycles
    For any edge (u,v)
    if:
        v is already visited and,
        v is an ancestor of u, meaning v was discovered before u, and,
        v is still under exploration (v's descendants are being explored)
    then:
        this is a back edge

Forward edge
    Connects a vertex to a descendant in the DFS tree. 
    Not part of the tree itself but connects vertices in a forward direction, that is vertex to one of its descendant that is not its direct child 
    for any edge (u,v)
    if:
        v is already visited,
        v is a descendant of u (discovered after u), and,
        v has finished exploration
    then: 
        this is a forward edge

'''

class Graph:
    def __init__(self,edges,n):
        self.n = n
        self.adjList = [[] for _ in range(n)]

        for (src,dest) in edges:
            self.adjList[src].append(dest)

def isDAG(edges,n) -> bool:
    G = Graph(edges,n)
    # lets calculate start, departure times
    visited = set()
    time = 0
    inStack = [False] * G.n
    discovery = [-1] * n
    finish = [-1] * n

    def dfs(s):
        nonlocal time
        visited.add(s)
        time += 1
        discovery[s] = time
        inStack[s] = True
        for neighbor in G.adjList[s]:
            if neighbor not in visited:
                if not dfs(neighbor):
                    return False
            elif inStack[neighbor]:
                return False
        time += 1
        finish[s] = time
        inStack[s] = False
        return True
    
    for i in range(G.n):
        if i not in visited:
            if not dfs(i):
                return False
    
    return True 

edges = [(0, 1), (0, 3), (1, 2), (1, 3), (3, 2), (3, 4), (3, 0), (5, 6), (6, 3)]
n = 7
output = False

assert isDAG(edges, n) == output