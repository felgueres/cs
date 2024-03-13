# Given a binary 2D matrix, find the number of islands. 
# A group of connected 1s forms an island. 
# For example, the below matrix contains 4 islands.

grid1 = [[1,1,0,0,0],
         [0,1,0,1,0],
         [1,1,0,1,0],
         [0,1,0,0,0],
         [0,0,0,0,0]]

grid2 = [[1,1,0,0,1],
         [0,1,0,0,0],
         [1,1,0,1,0],
         [0,0,0,0,0],
         [0,0,1,0,1]]

grid3 = [[1,1,0,0,1],
         [0,0,0,0,0],
         [1,1,0,1,0],
         [0,0,0,0,0],
         [1,0,1,0,1]]

grid4 = [[1,1,0,1,1],
         [0,1,0,0,0],
         [1,1,1,1,1],
         [0,0,1,0,0],
         [0,0,1,0,0]]

test_neighbors = [(grid1, (0,0), [(0,1),(1,1)])]

test_islands = [(grid1, 2),
                (grid2, 5),
                (grid3, 7),
                (grid4, 2)]

def get_neighbors(grid, source):
    directions = [(-1,0), (0,1), (1,0), (1,-1), (1,1)]
    neighbors = []
    row, col = source
    for (dy,dx) in directions:
        cur_row = row + dy 
        cur_col = col + dx
        if 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]) and grid[cur_row][cur_col] == 1:
            neighbors.append((cur_row,cur_col))
    return neighbors

assert get_neighbors(grid1, test_neighbors[0][1]) == test_neighbors[0][2]

def get_land(grid):
    lands = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                lands.append((row,col))
    return lands

def search_island(grid, source):
    path = [source] 
    visited = set()
    def dfs(s):
        for v in get_neighbors(grid, s): # find island neighbors on all directions
            if v not in visited:
                visited.add(v) # mark visited
                path.append(v) # add to path
                dfs(v) # unlike moving to next element in neighbors, you search for v, this is the depth piece
    dfs(source)
    return path

def get_islands(grid):
    visited = set()
    islands = 0

    def dfs(s):
        for v in get_neighbors(grid, s): # find island neighbors on all directions
            if v not in visited:
                visited.add(v) # mark visited
                dfs(v) # unlike moving to next element in neighbors, you search for v, this is the depth piece

    for land_point in get_land(grid):
        if land_point not in visited:
            islands += 1
            dfs(land_point)
    return islands 

for (grid, num_islands) in test_islands:
    res_num_islands = get_islands(grid)
    print(f"Expected {num_islands}, got: {res_num_islands}")
    assert res_num_islands == num_islands