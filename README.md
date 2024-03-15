# Algorithms

BFS. Path finding in trees or graphs
- Explore reachability and path length in trees and graphs 

DFS. Path finding in trees and graphs
- Edge types has info about relationship between edges 
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
- https://medium.com/techie-delight/top-25-depth-first-search-dfs-practice-problems-a620f0ab9faf