# Given an M × N binary matrix, replace all occurrences of 0’s by 1’s, 
# which are completely surrounded by 1’s from all sides (top, left, bottom, right, top-left, top-right, bottom-left, and bottom-right).

grid1 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

expected_grid1 = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

grid2 = [
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

expected_grid2 = [
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

grid3 = [
    [1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

expected_grid3 = [
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

grid4 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

expected_grid4 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

# identify patches, replace 
# | dfs or bfs on each zero 
# | then evaluate the boundary 
# | then flood 

def get_zeros(grid):
    res = []
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == 0:
                res.append((m,n))
    return res

def get_neighbors(s,grid):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    row,col = s
    neighbors = []

    for dy, dx in directions:
        c_row = row + dy
        c_col = col + dx
        if 0 <= c_row < len(grid) and 0 <= c_col < len(grid[0]):
            if grid[c_row][c_col] == 0:
                neighbors.append((c_row, c_col))
    return neighbors

def get_boundary(s,island,grid):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    row,col = s
    is_valid = []

    for dy, dx in directions:
        c_row = row + dy
        c_col = col + dx
        if 0 <= c_row < len(grid) and 0 <= c_col < len(grid[0]) and (grid[c_row][c_col] == 1 or (c_row, c_col) in island):
            is_valid.append(True)
        else:
            is_valid.append(False)
    return all(is_valid) 

assert set(get_neighbors((1,1), grid1)) == set([(1,2),(2,1),(2,2)]), f"Wrong neighbors"

def get_islands(grid):
    sources = get_zeros(grid)
    visited = set()
    islands = [] 

    def dfs(s, island):
        for neighbor in get_neighbors(s, grid):
            if neighbor not in visited:
                visited.add(neighbor) 
                island.append(neighbor)
                dfs(neighbor, island=island)

    for s in sources:
        if s not in visited: 
            island = [s]
            visited.add(s)
            islands.append(island)
            dfs(s, island)
    
    return islands 

def replace_surrounded(grid):
    islands = get_islands(grid)
    for island in islands:
        boundary_checks = [get_boundary(s,island,grid) for s in island]
        if all(boundary_checks):
            for s in island:
                row,col = s
                grid[row][col] = 1
    return grid

tests = [
    (grid1, expected_grid1),
    (grid2, expected_grid2),
    (grid3, expected_grid3)
]

for input,output in tests:
    answer = replace_surrounded(input) 
    assert answer == output, f"{answer}, expected: {output}"