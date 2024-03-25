'''
The transitive closure for a digraph G is a digraph G’ with an edge (i, j) corresponding to each directed path from i to j in G. 
The resultant digraph G’ representation in the form of the adjacency matrix is called the connectivity matrix.
Given a directed graph, return its connectivity matrix. The value of a cell C[i][j] in connectivity matrix C is 1 only if a directed path exists from vertex i to vertex j.

Input: Graph [edges = [(0, 2), (1, 0), (3, 1)], n = 4]
Output: [
	[1, 0, 1, 0],
	[1, 1, 1, 0],
	[0, 0, 1, 0],
	[1, 1, 1, 1]
]
Note that all diagonal elements in the connectivity matrix are 1 since a path exists from every vertex to itself.
'''
# Apply dfs on each node
# Save the paths
from collections import deque

edges = [(0, 2), (1, 0), (3, 1)]
n = 4

adj = {k:[] for k in range(n)}
for (u,v) in edges: adj[u].append(v)

ConnectivityMatrix = [[0 for x in range(n)] for y in range(n)]

# Method 1: DFS O(V^2)
def dfs(CM, root, desc):
    for neighbor in adj[desc]:
        if CM[root][neighbor] == 0:
            CM[root][neighbor] = 1
            dfs(CM,root,neighbor)

print('--dfs--')
for u in range(n):
    ConnectivityMatrix[u][u] = 1 # this is the diagonal
    dfs(ConnectivityMatrix, u, u) 
    print(ConnectivityMatrix[u])

# Method 2: BFS O(V^2)
CM = [[0 for x in range(n)] for y in range(n)]

def bfs():
    queue = deque()
    for u in range(n):
        queue.append((u,u))
        CM[u][u] = 1
        while queue:
            (r,c) = queue.popleft()
            for neighbor in adj[c]:
                if CM[r][neighbor] == 0:
                    CM[r][neighbor] = 1
                    queue.append((r,neighbor))

bfs()
print('--bfs--')
for row in range (n):
    print(CM[row])

# Methods 3: Floyd-Warshall O(V^3)

CM_FW = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n): CM_FW[i][i] = 1
for (u,v) in edges: CM_FW[u][v] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if CM_FW[i][k] and CM_FW[k][j]:
                CM_FW[i][j]=1

print('--floyd-warshall--')
for row in range (n):
    print(CM_FW[row])