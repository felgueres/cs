from collections import deque 

'''
Given a binary matrix where 0 represents water and 1 represents land, and connected ones form an island, count the total islands.
Input:
[
	[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	[1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
	[1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
	[0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
	[0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
	[1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
	[1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]
Output: 5
'''

# for all  1s, do bfs, count the bfs executions
mat = [
	[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
	[0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	[1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
	[1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
	[1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
	[0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
	[0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
	[1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
	[1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]

def get_neighbors(mat, source):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    neighbors = []
    for dy,dx in directions:
        cur_row = source[0]+dy
        cur_col = source[1]+dx
        if 0 <= cur_row < len(mat) and 0<= cur_col < len(mat[0]) and mat[cur_row][cur_col] == 1:
            neighbors.append((cur_row,cur_col))
    return neighbors

def bfs(mat,source,visited):
    queue = deque([source])
    while queue:
        cur_node = queue.popleft()
        for neighbor in get_neighbors(mat,cur_node):
            if neighbor not in visited:
                visited.add(neighbor) 
                queue.append(neighbor)

bfs_counter = 0
visited = set()
for m in range(len(mat)):
    for n in range(len(mat[0])):
        if mat[m][n] == 1 and (m,n) not in visited:
            bfs(mat, (m,n), visited)
            bfs_counter += 1

print(f'Islands: {bfs_counter}')