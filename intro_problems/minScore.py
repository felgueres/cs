# Minimum Score of a Path Between Two Cities

# You are given a positive integer n representing n cities numbered from 1 to n. 
# You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional 
# road between cities ai and bi with a distance equal to distancei. 
# The cities graph is not necessarily connected.
# The score of a path between two cities is defined as the minimum distance of a road in this path.
# Return the minimum possible score of a path between cities 1 and n.

# Note:
# A path is a sequence of roads between two cities.
# It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
# The test cases are generated such that there is at least one path between 1 and n.

# roads array, target, expected min score

test_case = ([[1,2,9],[2,3,6],[2,4,5],[1,4,7]], 4, 5)

def minScore(n:int, roads: list[list[int]]) -> int:
    adjacency_list = {i: [] for i in range(1, n+1)}  # Step 1: Initialize the adjacency list
    for road in roads:  # Step 2: Populate the adjacency list
        a, b, distance = road
        adjacency_list[a].append((b, distance))
        adjacency_list[b].append((a, distance))
    
    visited = set()
    min_score = float('inf')

    def dfs(src):
        nonlocal min_score
        visited.add(src)
        for neighbor, w in adjacency_list.get(src,[]):
            if neighbor not in visited:
                min_score = min(min_score,w)
                dfs(neighbor)
    
    dfs(n)

    return min_score

# This problem is pretty weird, its not representative or well defined

res = minScore(n=test_case[1], roads=test_case[0]) 
assert res == test_case[2]