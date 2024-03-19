# Algorithms

ELEMENTARY GRAPH ALGORITHMS

BFS. Path finding in trees or graphs
- Explore reachability and path length in trees and graphs 

DFS. Path finding in trees and graphs
- Edge types has info about relationship between edges 
- Backtracking properties. Reversible to previous state, ensures exploration of all paths 
- Keeping track of times. Serves to find timeline of exploration, useful for detecting cycles and understanding graph

Edges:
- tree edges. edge (u,v) if v first discovered by exploring (u,v)
- back edges. edge (u,v) connecting vertex u to ancestor v. self-loops in directed graphs are also back edges
- forward edges. edge (u,v) connecting vertex u to descendant v in tree. nontree edge
- cross edges. all other edges connecting vertices as long as one is not descendant on another

TopoSort. Order DAG such that for every vertex U to V, U comes before V in the ordering. Good for longest or shortest path finding in linear time
- Find shortest paths in linear time

Strongly Connected Components. Maximal set of vertices such that there is a path from U to V and a path from V to U (one way are not strongly connected)
- By decomposing into SCC you can analyze dependencies in networks like software modules, social graphs and websites

Minimum spanning trees (MST). Connects all weighted vertices with minimum total weight.
- Wire an electronic circuit with least amount of wire

Algos: MST-Generic, Kruskal, Prim, MST-Reduce

Problems
https://medium.com/techie-delight/top-25-depth-first-search-dfs-practice-problems-a620f0ab9faf

---

xReplace all occurrences of 0 that are surrounded by 1 in a binary matrix
xReplace all occurrences of 0 that are not surrounded by 1 in a binary matrix
xFlood Fill Algorithm
xFind length of the longest path in the matrix with consecutive characters
xFind the longest path in a Directed Acyclic Graph (DAG)
xFind endpoints for opposite colors (othello game) 
xDepth First Search (DFS) Implementation
xFind islands in matrix 
xTypes of edges involved in DFS and relation between them (Arrival Times Problem)
xTraverse given directory using DFS 
xFind all occurrences of a given string in a character matrix (dfs+backtrack)
xGenerate list of possible words from a character matrix (dfs+backtrack)
xFind the path between given vertices in a directed graph (dfs+backtrack)

---
Monday - Tuesday
Find the first k maximum occurring words in a given set of strings
Find cost of the shortest path in DAG using one pass of Bellman-Ford
Topological Sort Algorithm for DAG using DFS

P1 problems
Check if a graph is strongly connected or not using one DFS Traversal
Check if given digraph is a DAG (Directed Acyclic Graph) or not
Check if given graph is strongly connected or not
Check if undirected graph contains cycle or not
2-Edge Connectivity in a Graph
Determine if undirected graph is a Tree (Acyclic Connected Graph)
Determine if graph is Bipartite Graph using DFS
Transitive Closure of a Graph
Lexicographic sorting of given set of keys

Inorder, Preorder and Postorder Tree Traversal
Traverse given directory using BFS 
Find the maximum occurring word in a given set of strings (Trie)

---