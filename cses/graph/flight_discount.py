# https://cses.fi/problemset/task/1195
# scenario: min-price flight with x/2 variable on any flight
# one-way edges, min-price, weighted graph -> dijkstra's
# assumed positive prices
# output = minprice:int
# correct code, needs cpp performance

import sys
import heapq

num_cities, num_connections = map(int,sys.stdin.readline().split())
src = 1
dest = num_cities

adj_source = [[] for _ in range(num_cities + 1)]
adj_dest = [[] for _ in range(num_cities + 1)]
for _ in range(num_connections):
    s,d,w = map(int, sys.stdin.readline().strip().split())
    adj_source[s].append((d,w))
    adj_dest[d].append((s,w))

def min_distance(adj,s):
    discovered = [False]*(num_cities+1)
    distance = [float('inf')]*(num_cities+1)
    distance[s] = 0
    queue = [(0,s)]
    while queue:
        _,cur_node = heapq.heappop(queue)
        discovered[cur_node] = True
        for neig,w in adj[cur_node]:
            if not discovered[neig]:
                if distance[neig] > distance[cur_node]+w:
                    distance[neig] = distance[cur_node]+w
                    heapq.heappush(queue, (distance[neig], neig))
    return distance

dist_from_source = min_distance(adj_source, src)
dist_from_dest = min_distance(adj_dest, dest)
ans = dist_from_source[dest]

for city in range(1,num_cities+1):
    for v,edge_cost in adj_source[city]:
        ans = min(ans, dist_from_source[city] + edge_cost//2 + dist_from_dest[v])
print(ans)
