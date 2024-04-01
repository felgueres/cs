'''
Given a rectangular field with few sensors present, cross it by taking the shortest safe route without activating the sensors.
The rectangular field is in the form of an `M × N` matrix, find the shortest path from any cell in the first column to any cell in the last column of the matrix. 
The sensors are marked by the value 0 in the matrix, and all its eight adjacent cells can also activate the sensors. 
The path can only be constructed out of cells having value 1, and at any given moment, you are only allowed to move one step in either of the 4 directions - Up, Left, Down, Right.

Input:
Output: 11

The shortest safe path has a length of 11, and the route is marked in green below.
The solution should return -1 if there is no safe route to reach the destination.
'''

mat = [
	[0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def get_candidates(mat, source):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    candidates=[]
    for dy, dx in directions:
        cur_row = source[0]+dy
        cur_col = source[1]+dx
        if 0 <= cur_row < len(mat) and 0 <= cur_col < len(mat[0]) and mat[cur_row][cur_col] == 1:
            candidates.append((cur_row,cur_col))
    return candidates

from collections import deque
s = (1,0)
queue = deque([(s,0)])
visited = {s: None}
while queue:
    cur, dist = queue.popleft()

    if cur[1] == len(mat[0])-1:
        print(f"Crossed with distance: {dist}")
        break

    for candidate in get_candidates(mat,cur):
        if candidate not in visited:
            queue.append((candidate,dist+1))
            visited[candidate] = cur # creates bfs tree / predecessor graph

def print_path(G, source, destination):
    if source == destination:
        print(source)
    elif G.get(destination,None) is None:
        print("No path found")
    else:
        print_path(G, source, G.get(destination))
        print(destination)

print_path(visited, (1,0), (2,9))
    