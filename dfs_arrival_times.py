# Given a graph, find the arrival and departure time of its vertices in DFS. 
# The arrival time is the time at which the vertex was explored for the first time in the DFS, 
# and departure time is the time at which we have explored all the neighbors of the vertex, and we are ready to backtrack.

edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
nodes = 8 # 0 to 7

adj = {k:[] for k in range(nodes)}
for u,v in edges: adj[u].append(v)

time = 0
visited = set()
timeline = {k:[] for k in range(nodes)}

def dfs(u):
    global time
    visited.add(u)
    time += 1
    timeline[u].append(time)
    for v in adj.get(u,[]):
        if v not in visited:
            dfs(v)
    time += 1
    timeline[u].append(time)

for u in range(nodes):
    if u not in visited:
        dfs(u) 

print(timeline)