# Given a weighted directed acyclic graph (DAG) and a source vertex, 
# find the shortest path’s cost from the source vertex to all other vertices present in the graph. 
# If the vertex can’t be reached from the given source vertex, return its distance as infinity.

# SOME THEORY
# =========== 

# INITIALIZE-SINGLE-SOURCE(G,s)
# for each vertex v in G.V
#     v.d = inf
#     v.pi = nil
# s.d = 0

# RELAX(u,v,w) # tests whether we can improve the path by going through u 
# if v.d > u.d + w(u.v)
#     v.d = u.d + w(u.v)
#     v.pi = u

# DAG-SHORTEST-PATHS(G,w,s)
# topo sort vertices of G // (V+E) 
# INITIALIZE-SINGLE-SOURCE(G,s) // (V)
# for each vertex u, taken in topo sort order
#   for each vertex v in G.adj[u]
#       RELAX(u,v,w)
# So overall total running time (V+E) which is linear in the siZe of adj-list

edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), 
         (1, 6, 8), (3, 0, 3), (3, 4, 5), 
         (5, 1, 2), (7, 0, 6), (7, 1, -1), 
         (7, 3, 4), (7, 5, -4)]

n = 8
src = 7
dest = 2
output: 6

adj_l = { k:[] for k in range(8) }
for (s,d,w) in edges: 
    adj_l[s].append((d,w))

visited = set()
topo = []

# This is equilavent to INIT-SINGLE-SOURCE
pred = {k: None for k in range(n)} # predecessor of vertex
dist = {k: float('inf') for k in range(n)} # distance from source to vertex
dist[src] = 0 # distance from source to itself is 0

def toposort(s):
    if s not in visited:
        visited.add(s)
        for (d,_) in adj_l.get(s,[]):
            toposort(d)
        topo.append(s)

toposort(src)
topo = list(reversed(topo))
print(f"topo:{topo}")

def relax(u,v,w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        pred[v] = u

for u in topo:
    for v,w in adj_l.get(u,[]):
        relax(u,v,w)

def print_path(src, dest, pred):
    if dest == src:
        print(src, end=' ')
    elif pred[dest] is None:
        print("No path exists", end=' ')
    else:
        print_path(src, pred[dest], pred)
        print(dest, end=' ')

print(f'Distance from source {src} to all vertices: {dist}')
print(f'Shortest path cost from {src} to {dest}: {dist[dest]}')
print("Shortest path from {} to {}: ".format(src, dest), end='')
print_path(src, dest, pred)
