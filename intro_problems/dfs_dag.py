# Given a weighted directed acyclic graph (DAG) and two vertices - source and destination, find the greatest cost path from the source vertex to the destination vertex.
# Input: 
# Graph [edges = [(0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3), (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)], n = 8]
# src = 7, dest = 2
# Output: -5
# Note: Edge (x, y, w) represents an edge from x to y having weight w.

from graphviz import Digraph

def visualize_graph(edges):
    dot = Digraph()
    # Add edges with weights
    for (source, dest, weight) in edges:
        dot.edge(str(source), str(dest), label=str(weight))
    # Render the graph to a file (e.g., 'graphviz_output.png') and display it
    dot.render('graph', format='png', cleanup=True)
    return dot

edges = [(0, 6, 2), 
         (1, 2, -4), 
         (1, 4, 1), 
         (1, 6, 8), 
         (3, 0, 3), 
         (3, 4, 5), 
         (5, 1, 2), 
         (7, 0, 6), 
         (7, 1, -1), 
         (7, 3, 4), 
         (7, 5, -4)]

def get_adj_list(edges):
    adj_list = {}
    nodes = max([max(s,d) for (s,d,_) in edges])
    adj_list = {k: [] for k in range(nodes+1)}
    for (s,d,w) in edges:
        adj_list[s].append((d,w))
    return adj_list

def find_paths(source,destination,edges):
    adj_list = get_adj_list(edges)
    all_paths = []

    def dfs(current_path, current_weight):
        last_node = current_path[-1]
        if last_node == destination:
            all_paths.append((current_path, current_weight))
            return

        for node, weight in adj_list.get(last_node,[]):
            if node not in current_path:
                dfs(current_path + [node], current_weight+weight)

    dfs([source], 0)
    return all_paths 

# paths = find_paths(7,2, edges)
# print(sorted(paths, key=lambda x: x[1], reverse=True)[0][1])

# notes:
# because it's a dag, you are guaranteed no cycles so you can skip the visited element of dfs 
# checking the current path is analogous the checking the visited element, paths are unique

def topological_sort(edges, n):
    adj_list = {i: [] for i in range(n)}
    for s, d, _ in edges:
        adj_list[s].append(d)

    visited = set()
    topo = []

    def dfs(v):
        if v not in visited:
            visited.add(v)
            for child in adj_list[v]:
                dfs(child)
            topo.append(v)

    for v in range(n):
        if v not in visited:
            dfs(v)

    return topo[::-1]  # Reverse to get the correct order


def longest_path(edges, n, src, dest):
    adj_list = get_adj_list(edges)
    topo_order = topological_sort(edges, n)
    
    # Initialize distances
    distance = {v: float('-inf') for v in range(n)}
    distance[src] = 0

    for v in topo_order:
        if distance[v] != float('-inf'): # relax // update distannes for v if v is reachable from source
            print(f'v-> {v}')
            print(f'{distance}')
            for u, w in adj_list[v]:
                if distance[u] < distance[v] + w:
                    distance[u] = distance[v] + w

    return distance[dest]

longest_path = longest_path(edges, 8, 7, 2)
print(longest_path)

