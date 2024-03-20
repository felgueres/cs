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

# Bellman-Ford - Solves the single-source shortest-paths problem in the genreal case where edge weight may be negative
# It returns a boolean whether or not there is a negative-weight cycle that is reachable from the source
# If there's no such cycle, it produces the shortest paths and their weights

# BELLMAN-FORD(G,w,s)
#     INITIALIZE-SINGLE_SOURCE(G,s)
#     for i = 1 to |G.V| - 1
#         for each edge (u,v) in G.E
#             RELAX(u,v,w)
#     for each edge (u,v) in G.E
#         if v.d > u.d + w(u,v)
#             return False
#     return True

edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), 
         (1, 6, 8), (3, 0, 3), (3, 4, 5), 
         (5, 1, 2), (7, 0, 6), (7, 1, -1), 
         (7, 3, 4), (7, 5, -4)]

n = 8
src = 7
dest = 2
output: 6

# init single source G,s
dist = {k: float('inf') for k in range(n)} # for each vertex, v.d = inf
pred = {k: None for k in range(n)} # for each vertex, v.pi = nil
dist[src] = 0 # distance from source to itself is 0

def relax(u,v,w):
    if dist[v] > dist[u] + w:
        dist[v] = dist[u] + w
        pred[v] = u

for i in range(n-1):
    for (s,d,w) in edges:
        relax(s,d,w)

for (s,d,w) in edges:
    if dist[d] > dist[s] + w:
        print("Negative cycle.")

print('No negative cycles.')

def print_path(s,d,pred):
    if s == d:
        print(s, end=' ')
    elif pred[d] is None:
        print('No path found')
    else:
        print_path(s, pred[d],pred)
        print(d, end=' ')

print(f'Distance from source {src} to all vertices: {dist}')
print(f'Shortest path cost from {src} to {dest}: {dist[dest]}')
print("Shortest path from {} to {}: ".format(src, dest), end='')
print_path(src,dest,pred)
