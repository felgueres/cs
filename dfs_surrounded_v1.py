# Given an M × N binary matrix, replace all occurrences of 0’s by 1’s, 
# which are completely surrounded by 1’s from all sides (top, left, bottom, right, top-left, top-right, bottom-left, and bottom-right).

grid1 = [
    [1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

expected_grid1 = [
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

tests = [ (grid1, expected_grid1) ]

# Steps:
# Find 0 islands -> dfs or bfs
# Check is_surrounded
# Fill
visited = set()
islands = []

# keep track of the islands separately

def find_neighbors(source, grid):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] 
    row,col = source
    neighbors = []
    for (dy,dx) in directions:
        cur_row = row + dy
        cur_col = col + dx
        if 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]) and grid[cur_row][cur_col] == 0:
            neighbors.append((cur_row,cur_col))
    return neighbors

def dfs(source, island):
    visited.add(source)
    for neighbor in find_neighbors(source, grid1):
        if neighbor not in visited:
            row,col = neighbor
            island.append((row,col))
            dfs(neighbor, island)

for m in range(len(grid1)):
    for n in range(len(grid1[0])):
        island = []
        if grid1[m][n] == 0:
            if (m,n) not in visited:
                island.append((m,n))
                dfs((m,n), island)
                islands.append(island)

# implement check boundary
def check_boundary(s,path,grid):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] 
    row,col = s 
    valid = []
    for (dy,dx) in directions:
        cur_row = row + dy
        cur_col = col + dx
        if 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]) and (grid[cur_row][cur_col] == 1 or (cur_row,cur_col) in path):
            valid.append(True)
        else:
            break
    return valid 

for path in islands:
    is_fill = 0  
    for s in path: 
        is_valid = check_boundary(s,path,grid1)
        is_fill += sum(is_valid)
    if is_fill == len(path)*8:
        print(f'path will be filled: {path}')
        for (row,col) in path:
            grid1[row][col] = 1
    else:
        print(f'no path filled: {path}')

assert grid1 == expected_grid1, f'path doesnt match, {grid1} vs. {expected_grid1}'