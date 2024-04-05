'''
Given an undirected graph, determine whether it contains any cycle.

Input: Graph [edges = [(0, 1), (1, 2), (0, 2)], n = 3]
Output: True

Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (1, 4)], n = 5]
Output: False

Scenario
- Undirected
- Unweighted
- Has cycle

Ideas
- Build BFS tree
- Keep track of path 
- While traversing, does it loop back to itself?
- Is it strongly connected?
- A cross-edge points to a prev discovered vertex that is neither an ancestor nor descendant of current vertex
'''

from collections import deque

def has_cycle_bfs(edges, n):
    # BFS approach 
    src = 0
    queue = deque([(src, -1)]) 
    visited = set()
    visited.add(src)

    adj={i:[]for i in range(n)}
    for u,v in edges: 
        adj[u].append(v)
        adj[v].append(u) # because its undirected

    while queue:
        node, parent = queue.popleft()
        for neighbor in adj.get(node,[]):
            if neighbor not in visited:
                queue.append((neighbor,node))
                visited.add(neighbor)
            elif neighbor != parent:
                return True
    return False

def has_cycle_dfs(edges,n):
    adj={i:[]for i in range(n)}
    for u,v in edges: 
        adj[u].append(v)
        adj[v].append(u) # because its undirected
    visited = set()

    def dfs(node,parent):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                if dfs(neighbor,node):
                    return True 
            elif neighbor!=parent:
                return True
        return False

    src = 0

    has_cycle = dfs(src, -1)
    return has_cycle

tests = [([(0, 1), (1, 2), (0, 2)], 3, True),
        ([(0, 1), (1, 2), (2, 3), (1, 4)], 5, False)]

for i, (edges, n, exp) in enumerate(tests):
    assert has_cycle_bfs(edges,n) == exp, f'test{i}: wrong answer, expected {exp}'
    assert has_cycle_dfs(edges,n) == exp, f'test{i}: wrong answer, expected {exp}'
