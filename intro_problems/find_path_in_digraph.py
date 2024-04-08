'''

# Given a directed graph and two vertices - source and destination, determine if the destination vertex is reachable from the source vertex. 
The solution should return true if a path exists from the source vertex to the destination vertex, false otherwise.

Output: Bool

# Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)], n = 6], src = 4, dest = 5
# Output: True
# Explanation: There exist a path [4 —> 1 —> 2 —> 3 —> 5] from vertex 4 to vertex 5.

# Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)], n = 6], src = 5, dest = 1
# Output: False
# Explanation: There is no path from vertex 5 to any other vertex.

Scenario:
- Directed, find_path, non-weighted
- DFS or BFS is good option 
- Use global visited set to limit path exploration 

'''
from collections import deque

def is_reachable(edges, source, destination, n):
    visited = set()

    adj = {k:[] for k in range(n)}
    for u,v in edges:
        adj[u].append(v)

    queue = deque([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for neighbor in adj.get(node,[]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return False

edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)]
edges_2 = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)]

assert is_reachable(edges,4,5,6) == True, 'Test 1 fails'
assert is_reachable(edges_2,5,1,6) == False, 'Test 2 fails'