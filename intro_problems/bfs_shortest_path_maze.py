'''
Given a maze in the form of a binary rectangular matrix, find the length of the shortest path from a given source to a given destination. 
The path can only be constructed out of cells having value 1, and at any moment, you can only move one step in one of the four directions (Top, Left, Down, Right).

Output: 12

'''
matrix = [
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
	[1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
	[0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
	[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
	[0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
src  = (0, 0)
dest = (5, 7)
visited = set()
from collections import deque

def get_moves(matrix, s):
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    row,col = s
    print(f"{row}, {col}")
    moves = []
    for dy,dx in directions:
        cur_col = col + dy
        cur_row = row + dx
        if 0 <= cur_col < len(matrix) and 0 <= cur_row < len(matrix[0]) and matrix[cur_row][cur_col] == 1:
            moves.append((cur_row,cur_col))
    return moves

visited = {src: None} 
queue = deque([(src,0)])

while queue:
    cur,dist = queue.popleft()
    print(f"cur {cur}, dist {dist}")
    if cur == dest:
        print(f"Found it! Cur {cur} Dest {dest} with distance: {dist}")
        break

    for neighbor in get_moves(matrix,cur):
        print(neighbor)
        if neighbor not in visited:
            queue.append((neighbor,dist+1))
            visited[neighbor] = cur

def print_path(P,source,destination):
    if destination == source:
        print(source)
    elif P.get(destination,None) is None:
        print("No path")
    else:
        print_path(P, source, P[destination])
        print(destination)

print_path(visited, (0,0), (5,7))

# Scanning the neighbors is O(M*N), multiplicative complexity