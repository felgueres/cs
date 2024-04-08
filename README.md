# CS 

## DATA STRUCTURES

### Basic ops on dynamic sets


| OP | Description |
| --- | ---------- | 
| SEARCH(S,k) | Given set S and key valu k, return pointer x to an element in S such that x.key = k, or nil if no such element |
| INSERT(S,x) | Augment set S with the element pointed to by x. |
| DELETE(S,x) | Given a pointer x to an element in the S, removes x from S. Note this takes a pointer to an element x, not a key value
| MINIMUM(S) | Query on ordered set that returns a pointer to the element of S with the smallest key
| MAXIMUM(S) | Query on ordered set that returns a pointer to the element of S with the largest key 
| SUCCESSOR(S,x) | Given an element x whose key is from a totally ordered set S, returns a pointer to the next larger element in S, or nil if x is the maximum element
| PREDECESSOR(S,x) | Given an element x whose key is from a totally ordered set S, returns a pointer to the next smaller element in S, or nil if x is the minimum element

**STACK** Insert is called PUSH and DELETE is called a POP. Stacks and queues are dynamic sets in which the element removed is prespecified, so they don't take an element arg.

Stacks are implemented with an array. The array has an attribute S.top that indexes the most recently inserted element.

```js
STACK-EMPTY(S)
if S.top == 0:
    return TRUE
else return FALSE

// Takes O(1) time
```

```js
PUSH(S,x)
S.top = S.top + 1
S[S.top] = x

// Takes O(1) time
```
```js
POP(S)
if STACK-EMPTY(S) 
    error "underflow"
else S.top = S.top - 1
    return S[S.top + 1]

// Takes O(1) time
```

**QUEUES** Insert op is called ENQUEUE and delete DEQUEUE - both dont take an element argument. Queue has a head and a tail. When element is inserted it takes its place on the tail. The element dequeued is always the one at the head.

Queue has attribute Q.head that points or indexes its head, and an attribute Q.tail that indexes the next location at which a new item will arrive. The elements reside between Q.head ... Q.tail - 1, ie. Q.tail is free.

When Q.tail = Q.head, queue is empty, if dequeue, queue underflows.

Q.tail = Q.head = 1 initially.

When Q.head = Q.tail + 1, queue is full, if you enqueue its a queue overflow

```js
ENQUEUE(Q,x)
    Q[Q.tail] = x
if Q.tail == Q.length
    Q.tail = 1 // means the head = tail, its full
else Q.tail = Q.tail + 1 // point to new space

// Takes O(1) time
```

```js
DEQUEUE(Q)
x = Q[Q.head]
if Q.head == Q.length:
    Q.head = 1
else Q.head = Q.head + 1
return x

// Takes O(1) time
```

**LINKEDLISTS** Objects are arranged in linear order but unlike arrays where order is determined by indices, the order in a linked list is determined by a pointer in each object. LL support all basic ops, although not efficiently. 

The doubly linked list is an object with attribute key and two other pointer attributes: next and prev. The object may contain other satellite data. 

If x.prev = nil, x has no predecessor which means it's the head. if x.next = nil, it's the tail.

| List Form | Attributes | 
| --------- | ----------- |
| Singly    | No prev pointer |
| Doubly    | Has both pointers |
| Sorted    | Linearly order by key. Min key value is the head. Max key is the head |
| Unsorted  | Any order | 
| Circular  | Prev pointer of the head points to the tail |  
| Non-circular | Head has no prev pointer to tail | 

```js
LIST-SEARCH(L,k)
x = L.head
while x != nil and x.key != k:
    x = x.next
return x

//Takes O(n) time since it may have to search the entire list in the worst case
```

```js
LIST-INSERT(L,k)
x.next = L.head
if L.head != nil:
    L.head.prev = x
L.head = x
x.prev = nil

//This insert is on head, making k the first element (pushing the head to the right). Relevant when implementing a stack. Requires no traversal of the list.
// Inserting using the head or tail pointer is O(1), inserting in arbitrary position is worst-case O(n)

```

```js
LIST-DELETE(L,x)
// x is a pointer. this splices x out of the list by updating pointers
// to delete for a given key, you first need to LIST-SEARCH its pointer
if x.prev != nil:
    x.prev.next = x.next
else L.head = x.next
if x.next != nil
    x.next.prev = x.prev

// Deleteing runs in O(1) but if you wish to delete an element with a given key, takes O(n) because you first need to find the index for it. 
```
Introduction to algorithms, pg. 239

**Sentinels** help you ignore the boundary conditions at head and tail, which make it easier to code.

Suppose you provide with list L an object L.nil that represents NIL but has all the attributes of other objects in the list.
Whenever you have a reference to Nil in list code, you can replace it with L.nil

Using a sentinel or dummy, you can replace references, eliminate the need to keep L.head and L.tail attributes.

So you get:

```js
LIST-SEARCH'(L,k)
x = L.nil.next
while x!=L.nil and x.key!=k
    x = x.next
return x
```

```js
LIST-DELETE'(L,x)
x.prev.next = x.next
x.next.prev = x.prev
```

```js
LIST-INSERT'(L,x)
x.next = L.nil.next // L.nil.next points to current head of list
L.nil.next.prev = x  // L.nil.next.prev is prev from current head of list
L.nil.next = x // L.nil.next now replaces current head to new inserted 
x.prev = L.nil // Point the new head to L.nil again
```

## GRAPHS 

**BFS**. Path finding in trees or graphs
- Uses FIFO queue, eg. adds from the right, takes from the left, [1,2,3,4]  1 got in first and will be popped out first too
- Explore reachability and path length in trees and graphs 
- Shortest paths for unweighted graphs
- Minimum Spanning Trees for unweighted graphs
- Serial/Deserial of binary tree
- The ops of dequeing and queuing is constant - O(1) -, so total time devoted to queing and dequeing is O(V), scanning the adjency lists take O(E), therefore this algo takes O(V+E) 


**DFS**. Path finding in trees and graphs
- Edge types has info about relationship between edges 
- Backtracking properties. Reversible to previous state, ensures exploration of all paths 
- Keeping track of times. Serves to find timeline of exploration, useful for detecting cycles and understanding graph
- Complexity in its base case is O(V+E) on an adj list and O(V^2) on a matrix
- Initalizing the algo takes V, visiting the nodes takes E 

**Edge types**
- tree edges. edge (u,v) if v first discovered by exploring (u,v)
- back edges. edge (u,v) connecting vertex u to ancestor v. self-loops in directed graphs are also back edges
- forward edges. edge (u,v) connecting vertex u to descendant v in tree. nontree edge
- cross edges. all other edges connecting vertices as long as one is not descendant on another

**Relaxation**
- For each vertex v in V, maintain an attribute v.d, which is an upper bound on the weight of a shortest path
- Tests whether we can improve shortest path to v found so far by going through u, if so, updating v.d and v.pi
- Shortest paths differ in how many times you relax per edge, Djisktra exactly once, Bellman-Ford (V-1) 
- Note that bellman-ford is designed for digraphs, using on undigraphs is super complex 

**TopoSort**. Order DAG such that for every vertex U to V, U comes before V in the ordering. 
- Good for longest or shortest path finding in linear time

**Strongly Connected Components**. Maximal set of vertices such that there is a path from U to V and a path from V to U (one way are not strongly connected)
- By decomposing into SCC you can analyze dependencies in networks like software modules, social graphs and websites
- SCC uses \( G \) transposed, \( G^{T} \), which is the edges of \(G\) with edge directions reversed 
- Given adjacency -list representation of G, time to create \( G^{T} \) is \( O (V+E) \)
- SCC is computed using 2 dfs, one on \( G \) and another on \( G_{T} \)
- The first dfs pass gets you sorted graph by desc order of finishing times to ensure that on the second pass you can isolate the SCC in a single dfs per SCC. When you start the 2nd dfs from the highest finishing time and in order, you will cover all vertices within a single SCC before moving to another SCC. The reversal of edges prevents you to reach another SCC, effectively isolating each SCC per DFS call 

```js
STRONGLY-CONNECTED-COMPONENTS(G)
1 call DFS(G) to compute finish times u.f for each vertex u 
2 create G transposed
3 call DFS(Gt), but in the main loop DFS, consider vertices in order of decreasing u.f
4 output the vertices of each tree in the depth-first formed in line 3 as a separate strongly connected component
```
**k-edge-connected graph**. A connected graph is k-edge-connected if it remains connected whenever fewer than k edges are removed. Edge connectivity of a graph is the largest k for which the graph is k-edge-connected.
- A 2-edge-connected graph means you can delete any one edge and the graph will still be connected, it's often used to determine network redundancy  
- A bridge of \( G \) is an edge whose removal disconnects G
- An articulation point of \( G \) is a vertex whose removal disconnects \( G \)

**Finding Bridge Edges** 
Time: \(O(V + E)\)

An edge \((v,to)\) is a bridge iff none of the vertices \(to\) and its descendants in the DFS tree has a back-edge to vertex v or any ancestor.

Meaning that there's no way from \(v\) to \(to\) except for edge \((v,to)\)

You can infer this from 'time of entry into node'.

$tin[v]$  denote entry time for node  
$low$   array which will let us check the fact for each vertex $v$ 
$low[v]$  is the minimum of:  
- $tin[v]$ 
- the entry times $tin[p]$  for each node $p$  that is connected to node $v$  via a back-edge $(v, p)$ 
- $low[to]$ for each vertex $to$ which is a direct descendant of $v$  in the DFS tree

There is a back edge from vertex $v$ or one of its  descendants to one of its ancestors if and only if vertex $v$ has a child $to$ for which $low[v]$ < $tin[v]$.

If $low[v]$ = $tin[v]$, the back edge comes directly to $v$, otherwise it comes to an ancestor of $v$.

Thus, \((v,to)\) in DFS is a bridge if and only if $low[to]$ > $tin[v]$

**Binary Search Trees**. All basic dynamic-set ops work are supported.

Basic ops on the binary search tree take time proportional to the height of the tree.

For a complete binary tree with *n nodes* run in \( O(log n) \) i

If the tree is a linear chain of *n nodes*, the same ops take \( O(n) \) worst time.

A variation, the red-black tree, guarantees a height of \( O(log n) \).

> Keys in BST satisfy:
> Let x be a node in a BST.
> If y is a node in the left subtree of x, then y.key <= x.key 
> If y is a node in the right subtree of x, then y.key >= x.key

This property enables:
- INORDER-TREE-WALK: Prints key of the root of a subtree *between* printing the values in its left subtree and printing those in the right subtree
- PREORDER-TREE-WALK: Prints the root *before* the values in either subtree.
- POSTORDER-TREE-WALK: Prints the root *after* the values in its subtrees.

```js
INORDER-TREE-WALK(x)
if x!= NIL
    INORDER-TREE-WALK(x.left)
    print(x.key)
    INORDER-TREE-WALK(x.right)

// Takes O(n) time to walk an n-node BST, the procedure calls itself twice per node 
```

TODO: Write why dynamic-set ops run on O(h) where h is the height of the tree

**Red-Black Trees** Red-black tree is a scheme to balance the tree in order to guarantee that basic dynamic-set ops take O(lg n) worst case instead of O(h).

RB-tree is a BST with one extra bit of storage per node - `color` - which is either red or black.

Colors help to constrain paths such that no path from the root to a leaf is more than twice  as any other, ie. the tree is balanced.

```py
class RBTreeNode:
    self.key
    self.color
    self.left
    self.right
```

Red-black properties
1. Every node is either red or black
2. Root is black
3. Every leaf (nil) is black
4. If a node is red, then both children are black
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes

TODO: 
- Implement basic ops on RBTREE
- Cover B-TREES, basic ops, B-TREE-SEARCH, B-TREE-CREATE, B-TREE-INSERT

**Minimum spanning trees (MST)**. Connects all weighted vertices with minimum total weight.
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

#### Problem sets

**CSES** https://cses.fi/problemset/list/
- Rounded problem set and intro to competitive programming 

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
xTotal paths in a digraph from a given source to a destination having exactly `m` edges
xLeast cost path in a digraph from a given source to a destination having exactly `m` edges
\\\Compute the least cost path in a weighted digraph using BFS
xCheck if an undirected graph contains a cycle or not
xFind the minimum depth of a binary tree
xFind the path between given vertices in a directed graph
Print all nodes of a perfect binary tree in a specific order
Level order traversal of a binary tree
Print right view of a binary tree

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
xCheck if undirected graph is a Tree (Acyclic Connected Graph)
xCheck if a graph is strongly connected 
xCheck if given directed graph is a DAG or not
xCheck if graph is Bipartite Graph using DFS
x2-Edge Connectivity in a Graph
xTransitive Closure of a Graph
xInorder, Preorder and Postorder Tree Traversal
 Find the maximum occurring word in a given set of strings
 Find the first k maximum occurring words in a given set of strings
 Lexicographic sorting of given set of keys


**LINKEDLISTS** http://cslibrary.stanford.edu/105/LinkedListProblems.pdf

 Network Delay Time
 Shortest Routes I