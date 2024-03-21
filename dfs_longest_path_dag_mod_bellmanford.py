# Given a weighted directed acyclic graph (DAG) and two vertices - source and destination, find the greatest cost path from the source vertex to the destination vertex.
# Input: 
# Graph [edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)], 
# n = 8, 
# src = 7, dest = 2
# Output: -5

# Note: Edge (x, y, w) represents an edge from x to y having weight w.


edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)]
n = 8
src = 7
dest = 2

adj_l = {i:[] for i in range(n)}
for (s,d,w) in edges: adj_l[s].append((d,w))

dist = {i:float('-inf') for i in range(n)}
pred = {i:None for i in range(n)}
dist[src] = 0

def relax(s,d,w):
    if dist[d] < dist[s] + w:
        dist[d] = dist[s] + w
        pred[d] = s

for i in range(n-1):
    for (o,d,w) in edges:
        relax(o,d,w)

def print_path(s,d,pred):
    if s == d:
        print(s)
    elif pred[d] is None:
        print('no path found') 
    else:
        print_path(s, pred[d], pred)
        print(d)

print_path(src,dest,pred)

# complexity of this algorithm is V*E
# to improve to V+E you'd do topo sort and one pass of the bellmanford instead of n-1