'''
Given a directed graph, determine whether it is strongly connected or not. 
A directed graph is said to be strongly connected if every vertex is reachable from every other vertex.


# Theory
# Run dfs pass from any vertex to sort it by finishing times 
# Run a second dfs pass on finishing time desc order and reversed edges
# For each dfs call you will have a strongly connected component 

# If you want to determine if strongly connected
# Run dfs from any vertex and check if all V were visited

'''

def is_strongly_connected(edges,n):
    # O(n)
    # Create an adj list
    adj = {k:[] for k in range(n)}
    for u,v in edges: adj[u].append(v)
    visited = set()
    last_visited = None


    def dfs(src): 
        nonlocal last_visited
        visited.add(src)
        last_visited = src
        for neighbor in adj.get(src,[]):
            if neighbor not in visited:
                dfs(neighbor)

    src = 0
    dfs(src)
    if len(visited) != n:
        return False
    
    visited = set()
    dfs(last_visited)
    return len(visited) == n

tests= [([(0, 1), (1, 2), (2, 0)],3,True),
([(0, 1), (1, 2), (0, 2)], 3,False),
([(0, 1)], 2,False)]

for i, (edges, n, output) in enumerate(tests):
    res = is_strongly_connected(edges,n)
    print(f"Test {i}: answer -> {res}")
    assert res == output, f"test {i}: expecting {output}, got {res}"