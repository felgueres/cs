# CS study 

2 weeks
GRAPHS  
MATRIX  
BACKTRACKING  

1 week
BINARY TREE  
BINARY SEARCH TREE  
B-TREE

1 week
DIVIDE & CONQUER  
SLIDING WINDOW  
TWO POINTERS  

2 week
LINKED LIST  
HASHMAP  
ARRAY / STRING  
STACK  
HEAP  
TRIE

1 week
DP  

Extra
BIT MANIPULATION  
MATH  

ELEMENTARY GRAPH ALGORITHMS

BFS. Path finding in trees or graphs
- Uses FIFO queue, eg. adds from the right, takes from the left, [1,2,3,4]  1 got in first and will be popped out first too
- Explore reachability and path length in trees and graphs 
- Shortest paths for unweighted graphs
- Minimum Spanning Trees for unweighted graphs
- Serial/Deserial of binary tree

Relaxation
- For each vertex v in V, maintain an attribute v.d, which is an upper bound on the weight of a shortest path
- Tests whether we can improve shortest path to v found so far by going through u, if so, updating v.d and v.pi
- Shortest paths differ in how many times you relax per edge, Djisktra exactly once, Bellman-Ford (V-1)  

DFS. Path finding in trees and graphs
- Edge types has info about relationship between edges 
- Backtracking properties. Reversible to previous state, ensures exploration of all paths 
- Keeping track of times. Serves to find timeline of exploration, useful for detecting cycles and understanding graph

Edges:
- tree edges. edge (u,v) if v first discovered by exploring (u,v)
- back edges. edge (u,v) connecting vertex u to ancestor v. self-loops in directed graphs are also back edges
- forward edges. edge (u,v) connecting vertex u to descendant v in tree. nontree edge
- cross edges. all other edges connecting vertices as long as one is not descendant on another

TopoSort. Order DAG such that for every vertex U to V, U comes before V in the ordering. 
- Good for longest or shortest path finding in linear time

Strongly Connected Components. Maximal set of vertices such that there is a path from U to V and a path from V to U (one way are not strongly connected)
- By decomposing into SCC you can analyze dependencies in networks like software modules, social graphs and websites

Minimum spanning trees (MST). Connects all weighted vertices with minimum total weight.
- Wire an electronic circuit with least amount of wire

Algos: MST-Generic, Kruskal, Prim, MST-Reduce

Problems
DFS: https://medium.com/techie-delight/top-25-depth-first-search-dfs-practice-problems-a620f0ab9faf
BFS: https://medium.com/techie-delight/top-20-breadth-first-search-bfs-practice-problems-ac2812283ab1

---
BFS
xBreadth-First Search (BFS)
xTransitive closure of a graph
xFind root vertex of a graph
Chess Knight Problem | Find the shortest path from source to destination
Shortest path in a maze — Lee Algorithm
Find the shortest safe route in a field with sensors present
Find the shortest path from source to destination in a matrix that satisfies given constraints
Check if a graph is strongly connected or not
Flood Fill Algorithm
Count number of islands
Find minimum passes required to convert all negative values in a matrix
Snake and Ladder Problem
Find the shortest distance of every cell from a landmine inside a maze
Check if an undirected graph contains a cycle or not
Find maximum cost path in a graph from a given source to a given destination
Total paths in a digraph from a given source to a destination having exactly `m` edges
Least cost path in a digraph from a given source to a destination having exactly `m` edges
Traverse a given directory using BFS and DFS in Java
Level order traversal of a binary tree
Depth-First Search (DFS) vs Breadth-First Search (BFS)
Bipartite Graph
Compute the least cost path in a weighted digraph using BFS
Find the path between given vertices in a directed graph
Print all nodes of a perfect binary tree in a specific order
Print right view of a binary tree
Find the minimum depth of a binary tree


DFS
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
xFind cost of the shortest path in DAG using one pass of Bellman-Ford
xFind cost of the longest path in DAG
xCheck if undirected graph contains cycle or not
 Check if undirected graph is a Tree (Acyclic Connected Graph)
 Check if given directed graph is a DAG or not
 Check if a graph is strongly connected or not using one DFS Traversal
 Check if given graph is strongly connected or not
 Check if graph is Bipartite Graph using DFS
 2-Edge Connectivity in a Graph
 Transitive Closure of a Graph
 Inorder, Preorder and Postorder Tree Traversal
 Find the maximum occurring word in a given set of strings
 Find the first k maximum occurring words in a given set of strings
 Lexicographic sorting of given set of keys