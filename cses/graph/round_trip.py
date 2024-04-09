# https://cses.fi/problemset/task/1669

import sys
sys.setrecursionlimit(10**6)
cities, roads = map(int,sys.stdin.readline().split())
adj = [[] for _ in range(cities+1)]
for _ in range(roads):
    src,dest = map(int,sys.stdin.readline().strip().split())
    adj[src].append(dest)
    adj[dest].append(src)

visited = [False] * (cities+1)
parent = [-1]*(cities+1)

def dfs(node,parent_node):
    visited[node]=True
    for neig in adj[node]:
        if not visited[neig]:
            parent[neig] = node
            if dfs(neig,node):
                return True 
        elif neig != parent_node:
            cycle = []
            current = node
            print(f'recontructing path from current node : {node}')
            print(f'predecessor arr: {parent}')
            while current != neig:
                # current is not neig 
                print(f"current {current} is not neigh: {neig}")
                cycle.append(current)
                current = parent[current]
            cycle.append(neig)
            cycle.append(node)
            cycle.reverse()
            print(len(cycle))
            print(' '.join(map(str,cycle)))
            return True
    return False 

found = False
for city in range(1,cities+1): 
    if not visited[city]:
        if dfs(city,-1):
            found = True
            break
            
if not found: print('IMPOSSIBLE')