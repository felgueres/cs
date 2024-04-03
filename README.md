# CS 

GRAPHS  
MATRIX  
BACKTRACKING  

BINARY TREE  
BINARY SEARCH TREE  
B-TREE

DIVIDE & CONQUER  
SLIDING WINDOW  
TWO POINTERS  

LINKED LIST  
HASHMAP  
ARRAY / STRING  
STACK  
HEAP  
TRIE

DP
BIT MANIPULATION  
MATH  

## GRAPH ALGORITHMS

BFS. Path finding in trees or graphs
- Uses FIFO queue, eg. adds from the right, takes from the left, [1,2,3,4]  1 got in first and will be popped out first too
- Explore reachability and path length in trees and graphs 
- Shortest paths for unweighted graphs
- Minimum Spanning Trees for unweighted graphs
- Serial/Deserial of binary tree
- The ops of dequeing and queuing is constant - O(1) -, so total time devoted to queing and dequeing is O(V), scanning the adjency lists take O(E), therefore this algo takes O(V+E) 

Relaxation
- For each vertex v in V, maintain an attribute v.d, which is an upper bound on the weight of a shortest path
- Tests whether we can improve shortest path to v found so far by going through u, if so, updating v.d and v.pi
- Shortest paths differ in how many times you relax per edge, Djisktra exactly once, Bellman-Ford (V-1) 
- Note that bellman-ford is designed for digraphs, using on undigraphs is super complex 

DFS. Path finding in trees and graphs
- Edge types has info about relationship between edges 
- Backtracking properties. Reversible to previous state, ensures exploration of all paths 
- Keeping track of times. Serves to find timeline of exploration, useful for detecting cycles and understanding graph
- Complexity in its base case is O(V+E) on an adj list and O(V^2) on a matrix
- Initalizing the algo takes V, visiting the nodes takes E 

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
- Algorithms: MST-Generic, Kruskal, Prim, MST-Reduce

#### Heuristics

| Scenario | Algorithm | Reason | Complexity |
| -------- | --------- | ------ | ---------- |
| Find shortest path in unweighted graph | BFS | Guarantess shortest path due to exploring level by level | V+E or V^2, adj vs matrix, V is when looping to initialize, E is when exploring edges 
| Unweighted directed graph | BFS | Ideal for unweighted (directed and indirected) as guarentees shortest path by exploring vertices in order of their distance to source | V + E for adjencent list |
| Find all paths | DFS | Easy to explore all paths. Useful when you don't necessarily need the shortest. | V+E or V^2, adj vs matrix, V is when looping to initialize, E is when exploring edges
| Find all paths | BFS | This requires a variation, relaxing the constraint of a global visit set. Lets you search all paths and add other constraints | V+E or V^2, adj vs matrix, V is when looping to initialize, E is when exploring edges
| Find shortest path in weighted graph with negative weights | Bellman-Ford | Relaxation helps find min cost paths and handles negative cycles | On acyclic, you can do V + E by using toposort, otherwise V^2
| Topo sort | DFS | Useful to improve performance on other alorithms like Bellman-Ford | V + E
| Minimum depth | BFS | Fits with level-by-level exploration | V + E
| Cycle detection in digraph
| Connected components 

#### Problem sets
**BFS** https://medium.com/techie-delight/top-20-breadth-first-search-bfs-practice-problems-ac2812283ab1

xBreadth-First Search (BFS)
xTransitive closure of a graph
xFind root vertex of a graph
xChess Knight Problem 
xShortest path in a maze — Lee Algorithm
xFind shortest safe route in a field with sensors present
\Find shortest path from source to destination in a matrix that satisfies given constraints 
xFlood Fill Algorithm
xCount number of islands
xFind minimum passes required to convert all negative values in a matrix
xFind the shortest distance of every cell from a landmine inside a maze
xFind maximum cost path in a graph from a given source to a given destination
xSnake and Ladder Problem
Total paths in a digraph from a given source to a destination having exactly `m` edges
Least cost path in a digraph from a given source to a destination having exactly `m` edges
Compute the least cost path in a weighted digraph using BFS
Check if an undirected graph contains a cycle or not
Check if a graph is strongly connected or not
Find the minimum depth of a binary tree
Find the path between given vertices in a directed graph
Print all nodes of a perfect binary tree in a specific order
Level order traversal of a binary tree
Print right view of a binary tree
Bipartite Graph

**DFS** https://medium.com/techie-delight/top-25-depth-first-search-dfs-practice-problems-a620f0ab9faf
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