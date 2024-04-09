# https://cses.fi/problemset/task/1197
# scenario: directed graph, weighted, find and print negative cycle
# djiktra wont work, needs to be bellman ford, runs O(VE)
# no adj
# TODO: Bellman-ford is intuitive but printing the cycle is not. Try again. 
 
import sys
n, m= map(int, sys.stdin.readline().split())
 
edges = []
for _ in range(m):
    _s,_d,_w = map(int,sys.stdin.readline().strip().split())
    edges.append((_s,_d,_w))
 
distances = [float('inf')]*(n+1)
pred = [None]*(n+1)
distances[1] = 0
 
for i in range(n-1):
    for u,v,w in edges:
        if distances[v] > distances[u]+w:
            distances[v] = distances[u]+w
            pred[v] = u
 
# if you can relax once more, that's a negative cycle
found_cycle=False
for u,v,w in edges:
    if distances[v] > distances[u]+w:
        found_cycle=True
        # recover path
        current = v
        path = []
        while current != 1:
            current = pred[current] 
            path.append(current)
        path.append(v)
        path.append(1)
        path = reversed(path)
        str_path = map(str,path)
        print(' '.join(str_path))
 
if not found_cycle:
    print("NO")
