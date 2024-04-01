'''
Given a maze in the form of a rectangular matrix, filled with either 'O', 'X', or 'M', where 'O' represents an open cell, 'X' represents a blocked cell, and 'M' represents landmines in the maze, find the shortest distance of every open cell in the maze from its nearest mine.
The task is to find the shortest distance of every open cell in the maze from its nearest mine. You are only allowed to travel in either of the four directions, and diagonal moves are not allowed. The cells with landmines have a distance of 0, and blocked/unreachable cells have a distance of -1.
Input:
mat = [
	['O', 'M', 'O', 'O', 'X'],
	['O', 'X', 'X', 'O', 'M'],
	['O', 'O', 'O', 'O', 'O'],
	['O', 'X', 'X', 'X', 'O'],
	['O', 'O', 'M', 'O', 'O'],
	['O', 'X', 'X', 'M', 'O']
]
Here, O (Open cell), X (Blocked Cell), and M (Landmine).
Output:
[
	[1,  0,  1,  2, -1],
	[2, -1, -1,  1,  0],
	[3,  4,  3,  2,  1],
	[3, -1, -1, -1,  2],
	[2,  1,  0,  1,  2],
	[3, -1, -1,  0,  1]
]

Task
- Find nearest mine distance for every open cell
- Valid moves [(-1,0),(0,1),(1,0),(0,-1)]
Method
- Run bfs on each node to get smallest distance
- Think of a heuristic to limit the depth on bfs, although bfs explore the boundary on incremental steps, that might already be optimal
- Perhaps by proximity to another cell you can infer the closest
- Break BFS on first finding, not need to create entire BFS tree
'''
def find_candidates(mat, source):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    candidates = []
    for dy,dx in directions:
        cur_r = source[0]+dy
        cur_c = source[1]+dx
        if 0 <= cur_r < len(mat) and 0 <= cur_c < len(mat[0]) and mat[cur_r][cur_c] != 'X':
            candidates.append((cur_r,cur_c))
    return candidates

from collections import deque
def bfs(mat,source):
    visited = set()
    queue = deque([(source,0)])
    while queue:
        s,dist = queue.popleft()
        for candidate in find_candidates(mat,s):

            if mat[candidate[0]][candidate[1]] == 'M':
                return dist + 1 
            
            if candidate not in visited:
                visited.add(candidate)
                queue.append((candidate,dist+1))
    return -1

mat = [
	['O', 'M', 'O', 'O', 'X'],
	['O', 'X', 'X', 'O', 'M'],
	['O', 'O', 'O', 'O', 'O'],
	['O', 'X', 'X', 'X', 'O'],
	['O', 'O', 'M', 'O', 'O'],
	['O', 'X', 'X', 'M', 'O']
]

for m in range(len(mat)):
    for n in range(len(mat[0])):
        if mat[m][n] == 'O':
            dist = bfs(mat, (m,n))
            mat[m][n] = dist

for m in range(len(mat)):
    for n in range(len(mat[0])):
        if mat[m][n] == 'X':
            mat[m][n] = -1
        elif mat[m][n] == 'M':
            mat[m][n] = 0

for r in mat: print(r)