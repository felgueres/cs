# Given an M × N binary matrix, replace all occurrences of 0’s by 1’s, 
# which are not completely surrounded by 1’s from all sides 

matrix = [
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
]
output = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Get connected Zeros 
# Check boundary
# Not convert number if surrounded

def get_neighbors(mat,source):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    row,col = source
    neighbors = []
    for dy,dx in directions:
        c_row = row + dy 
        c_col = col + dx
        if 0 <= c_row < len(mat) and 0 <= c_col < len(mat[0]) and mat[c_row][c_col] == 0:
            neighbors.append((c_row,c_col))
    return neighbors

def get_connected(mat):
    visited = set()
    paths = []

    def dfs(source, path):
        visited.add(source)
        path.append(source)
        for neighbor in get_neighbors(mat,source):
            if neighbor not in visited:
                dfs(neighbor, path)

    for m in range(len(mat)):
        for n in range(len(mat[0])):
            if (m,n) not in visited and mat[m][n] == 0:
                path = []
                dfs((m,n), path)
                if path:
                    paths.append(path)
    return paths

def is_surrounded(mat,path):
    directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    surrounded = []
    for source in path:
        row,col = source
        for dy,dx in directions:
            c_row = row + dy 
            c_col = col + dx
            if 0 <= c_row < len(mat) and 0 <= c_col < len(mat[0]) and (mat[c_row][c_col] == 1 or (c_row,c_col) in path):
                surrounded.append(True)
            else:
                surrounded.append(False)
    return all(surrounded)

paths = get_connected(matrix)

for path in paths:
    if not is_surrounded(matrix,path):
        for (row,col) in path:
            matrix[row][col] = 1

assert(matrix == output) 
print("test passed!")
