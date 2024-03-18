# Given a directed graph and two vertices - source and destination, determine if the destination vertex is reachable from the source vertex. 
# The solution should return true if a path exists from the source vertex to the destination vertex, false otherwise.
# 
# Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)], n = 6], src = 4, dest = 5
# Output: True
# Explanation: There exist a path [4 —> 1 —> 2 —> 3 —> 5] from vertex 4 to vertex 5.
# 
# Input: Graph [edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)], n = 6], src = 5, dest = 1
# Output: False
# Explanation: There is no path from vertex 5 to any other vertex.
# 
# Constraints:
# 
# • The graph is implemented using an adjacency list.
# • The maximum number of nodes in the graph is 100, i.e., 0 <= n < 100, and each node is represented by its numeric value.
# • The destination can be reached from the source.
# You want to backtrack if you don't find on the current path 

def find_path_directed_graph(edges,n,src,dest):
    adj_list = {i:[] for i in range(n)}
    final_path = []

    for s,d in edges: 
        adj_list[s].append(d)
    
    def dfs(src,path):
        if src == dest:
            final_path.append(path.copy())
            return

        for e in adj_list.get(src,[]):
            if e not in path:
                path.append(e)
                dfs(e, path)
                path.pop()

    dfs(src,[src])

    if final_path:
        return final_path
    else:
        return False

edges = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 1)]
print(find_path_directed_graph(edges,n=6,src=4,dest=5))
print(find_path_directed_graph(edges,n=6,src=5,dest=1))