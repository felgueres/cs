import sys
import heapq

v,e = map(int, sys.stdin.readline().split())
edges = []

for _ in range(e):
    a,b,w = map(int, sys.stdin.readline().split())
    edges.append((a,b,w))

# heapq is implemented as min heap in python
# think of the python heap as a list where heap[0] is the smallest item
# heap.sort() maintains the heap invariant of having the min element on the root
 
class Graph:
    def __init__(self, edges:list[tuple], n:int):
        self.adj = {k:[] for k in range(n)}
        self.n = n
        for u,v,w in edges: 
            self.adj[u-1].append((v-1,w)) #one way 

def shortest_route_lengths(graph:Graph):
    src = 0
    vertices = [{'id': u, 'dist': float('inf')} for u in range(graph.n)] # O(n)
    vertices[src]['dist'] = 0
    Q = [(0, src)]
    settled = set()
    while Q: # O(n)
        dist_u, u_id = heapq.heappop(Q) # O(1)
        if u_id in settled: continue # this means its settled
        settled.add(u_id)
        for v,w in graph.adj[u_id]: # O(n)
            if vertices[v]['dist']>dist_u+w:
                vertices[v]['dist']=dist_u+w
                heapq.heappush(Q, (vertices[v]['dist'],v)) # O(lg n)
    return [v['dist'] for v in vertices]

G = Graph(edges,v)
shortest = shortest_route_lengths(G)
str = " ".join(map(str,shortest))
print(str)

# The total time complexity for this is O(E log n)