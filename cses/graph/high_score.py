# https://cses.fi/problemset/task/1673

import sys
num_rooms,num_tunnels = map(int,sys.stdin.readline().split())
edges = []
for _ in range(num_tunnels):
    s,dest,w = map(int,sys.stdin.readline().strip().split())
    edges.append((s,dest,w))
# go from room 1 to room n
# scenario: weighted, one-way, cycles, negative weights
# perfect for bellman-ford, best runs at O(rooms*tunels)
# print max score or -1 if cycle allows infinite
# best with bellman-ford, modify relaxation to get max 

src = 1
dest = num_rooms
distances = [float('-inf')] * (num_rooms+1)
distances[src] = 0

for i in range(num_rooms+1):
    for u,v,w in edges:
        if distances[v] < (distances[u]+w):
            distances[v] = distances[u]+w

has_cycle = False 
cur_distance = distances[num_rooms]

for u,v,w in edges:
    if distances[v]<distances[u]+w:
        distances[v] = distances[u]+w

if cur_distance < distances[num_rooms]:
    print(-1)
else:
    print(cur_distance)
