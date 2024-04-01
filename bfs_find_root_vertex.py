# A root vertex of a digraph is a vertex u with a directed path from u to v for every pair
# of vertices in the graph can be reached from the root vertex.
# Ie.
#   a vertex that reaches ALL other vertices in the graph
#   a vertex that by traversing it you can get to n vertices
# A graph can have multiple root vertices.
# In a strongly connected component every vertex is a root vertex

# Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)], n = 6]
# Output: 4
# Explanation: The root vertex is 4 since it has a path to every other vertex in the graph

class Vertex:
    def __init__(self,value):
        self.val = value
        self.predecessor = None

edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 3), (4, 5), (5, 0)]
n=6
# This initialization takes O(V)
# The overhead of scanning the adj lists is O(E)
# So the BFS procedure is O(V+E)

adj = {k:[] for k in range(n)}
for u,v in edges: adj[u].append(v)

from collections import deque

def bfs(adj,start):
    visited = set()
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.add(u)
            for v in adj[u]:
                if v not in visited:
                    queue.append(v)
    return visited

root_vertices = []
for i in range(n):
    if len(bfs(adj,i)) == n:
        root_vertices.append(i)

print(f"root vertices: {root_vertices}")

# Since I'm running this one per source
# The worst case here is O(N*(V+E))
# You can simplify a bit because N is V so O((V+E)*V)
