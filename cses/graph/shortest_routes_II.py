# https://cses.fi/problemset/task/1672
# T1: 36mins50s, mistakes: discovery done on dequeue, use total distance from start node as priority in heap  

import sys
import heapq

num_cities,num_roads,num_queries = map(int,sys.stdin.readline().split())

adj=[[] for _ in range(num_cities+1)]
for _ in range(num_roads):
    u,v,w = map(int, sys.stdin.readline().strip().split())
    adj[u].append((v,w))
    adj[v].append((u,w))

queries = []
for _ in range(num_queries): 
    s,d = map(int, sys.stdin.readline().strip().split())
    queries.append((s,d))

# scenario -> weighted, positive wieghts, undirected, shortest path -> dijkstra
# output: query(s,d) -> distance:int
# reading and describing problem -> 10mins

# Time complexity: O(V * lg n)

def query(s,d,num_cities):
    discovered = [False] * (num_cities + 1)
    distances = [float('inf')] * (num_cities + 1)
    distances[s] = 0
    queue = [(0,s)]
    while queue:
        _, cur_node = heapq.heappop(queue) # O(1)
        discovered[cur_node] = True
        for (neig,w) in adj[cur_node]: # (V)
            if not discovered[neig]:
                if distances[neig] > distances[cur_node] + w:
                    distances[neig] = distances[cur_node] + w 
                    heapq.heappush(queue, (distances[neig],neig)) # tuple is w,key, where w is used to heapify O(ln n)
    return distances[d] if distances[d] != float('inf') else -1

for s,d in queries:
    print(query(s,d,num_cities))
