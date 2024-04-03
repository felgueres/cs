'''
Given a directed graph, two vertices - source and destination, and a positive number m, 
find the total number of routes to reach the destination vertex from the source vertex with exactly m edges.
Input: Graph [edges = [(0, 6), (0, 1), (1, 6), (1, 5), (1, 2), (2, 3), (3, 4), (5, 2), (5, 3), (5, 4), (6, 5), (7, 6), (7, 1)], n = 8], src = 0, dest = 3, m = 4
Output: 3
Explanation: The graph has 3 routes from source 0 to destination 3 with 4 edges.
0 —> 1 —> 5 —> 2 —> 3
0 —> 1 —> 6 —> 5 —> 3
0 —> 6 —> 5 —> 2 —> 3
'''

edges = [(0, 6), (0, 1), (1, 6), (1, 5), (1, 2), (2, 3), (3, 4), (5, 2), (5, 3), (5, 4), (6, 5), (7, 6), (7, 1)]

adj = {k:[] for k in range(8)}
for s,d in edges: adj[s].append(d)

from collections import deque
src = 0
dest = 3
m = 4

queue = deque([(src, 0, [src])])
path_count = 0
paths = []

while queue:
    node, dist, path = queue.popleft()
    if node == dest and dist == m:
        path_count += 1 
        paths.append(path)
    if dest > m:
        break 

    for neighbor in adj.get(node,[]):
        queue.append((neighbor, dist+1, path+[neighbor]))

print(path_count)
print(paths)