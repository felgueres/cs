'''
Given a weighted undirected graph, find the maximum cost path from the given source vertex to any other vertex which is greater than the given cost. 
The path should not contain any cycles.

Input: Graph [edges = [(0, 6, 11), (0, 1, 5), (1, 6, 3), (1, 5, 5), (1, 2, 7), (2, 3, -8), (3, 4, 10), (5, 2, -1), (5, 3, 9), (5, 4, 1), (6, 5, 2), (7, 6, 9), (7, 1, 6)], n = 8], source = 0, cost = 50
Here, tuple (x, y, w) represents an edge from x to y having weight w.

Output: 51

Explanation: The maximum cost route from the source vertex 0 to any other vertex in the graph is [0 —> 6 —> 7 —> 1 —> 2 —> 5 —> 3 —> 4]. 
Its cost is 51 which is more than the given cost 50.

If all paths from the source vertex have their costs less than the given cost, the solution should return -sys.maxsize.

Steps
Traverse all paths from source
For each step, check if any path meets criteria
When meets, break and print path

'''

edges = [(0, 6, 11), 
         (0, 1, 5), 
         (1, 6, 3), 
         (1, 5, 5), 
         (1, 2, 7), 
         (2, 3, -8), 
         (3, 4, 10), 
         (5, 2, -1), 
         (5, 3, 9), 
         (5, 4, 1), 
         (6, 5, 2), 
         (7, 6, 9), 
         (7, 1, 6),
         (7,2,20)]

n = 8
source = 0
cost = 50 

adj = {k:[] for k in range(n)}
for u,v,w in edges: 
    adj[u].append((v,w))
    # Since its undirected
    adj[v].append((u,w))

from collections import deque
# lets track the cumulative cost and path
queue = deque([(source,0,[source])])
paths = []

while queue:
    node,dist,path = queue.popleft()

    if dist > cost:
        paths.append((path, dist))

    for neighbor,neighbor_dist in adj.get(node):
        if neighbor not in path:
            queue.append((neighbor, dist+neighbor_dist, path+[neighbor])) 

max_path_val = -1 
max_path = None

for (p,v) in paths:
    if v > max_path_val:
        max_path_val = v
        max_path = p 

print(f"Max cost path greater than {cost}: {max_path} with {max_path_val}")