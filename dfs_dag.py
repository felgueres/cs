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

paths = find_paths(7,2, edges)
print(sorted(paths, key=lambda x: x[1], reverse=True)[0][1])

# notes:
# because it's a dag, you are guaranteed no cycles so you can skip the visited element of dfs 
# checking the current path is analogous the checking the visited element, paths are unique