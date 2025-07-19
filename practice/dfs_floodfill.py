'''

Flood fill is an algorithm that determines the area connected to a given node in a multi-dimensional array. 
When applied on an image to fill a particular bounded area with color, it is also known as boundary fill.

The flood fill algorithm takes three parameters: a start node, a target color, and a replacement color. 
The algorithm looks for all nodes in the matrix that are connected to the start node by a path of the target color and changes them to the replacement color.

Input:

Matrix = [
	[Y, Y, Y, G, G, G, G, G, G, G],
	[Y, Y, Y, Y, Y, Y, G, V, V, V],
	[G, G, G, G, G, G, G, V, V, V],
	[W, W, W, W, W, G, G, G, G, V],
	[W, R, R, R, R, R, G, V, V, V],
	[W, W, W, R, R, G, G, V, V, V],
	[W, B, W, R, R, R, R, R, R, V],
	[W, B, B, B, B, R, R, V, V, V],
	[W, B, B, V, B, B, B, B, V, V],
	[W, B, B, V, V, V, V, V, V, V]
]

Start node, having a target color `V`
(x, y) = (3, 9)
Replacement Color = O

Output:
[
	[Y, Y, Y, G, G, G, G, G, G, G],
	[Y, Y, Y, Y, Y, Y, G, O, O, O],
	[G, G, G, G, G, G, G, O, O, O],
	[W, W, W, W, W, G, G, G, G, O],
	[W, R, R, R, R, R, G, O, O, O],
	[W, W, W, R, R, G, G, O, O, O],
	[W, B, W, R, R, R, R, R, R, O],
	[W, B, B, B, B, R, R, O, O, O],
	[W, B, B, O, B, B, B, B, O, O],
	[W, B, B, O, O, O, O, O, O, O]
]
'''
# (x, y) = (0, 0)
# Replacement Color = O

grid1 = [
    ['Y', 'Y', 'B', 'C'],
    ['Y', 'Y', 'B', 'C'],
    ['Y', 'Y', 'B', 'C'],
]

expected1 = [
    ['O', 'O', 'B', 'C'],
    ['O', 'O', 'B', 'C'],
    ['O', 'O', 'B', 'C'],
]

grid2 = [
    ['Y', 'A', 'B', 'C'],
    ['Y', 'Y', 'Y', 'Y'],
    ['A', 'A', 'B', 'Y'],
]

expected2 = [
    ['P', 'A', 'B', 'C'],
    ['P', 'P', 'P', 'P'],
    ['A', 'A', 'B', 'P'],
]

grid3 = [
    ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
    ["Y", "Y", "Y", "Y", "Y", "Y", "G", "V", "V", "V"],
    ["G", "G", "G", "G", "G", "G", "G", "V", "V", "V"],
    ["W", "W", "W", "W", "W", "G", "G", "G", "G", "V"],
    ["W", "R", "R", "R", "R", "R", "G", "V", "V", "V"],
    ["W", "W", "W", "R", "R", "G", "G", "V", "V", "V"],
    ["W", "B", "W", "R", "R", "R", "R", "R", "R", "V"],
    ["W", "B", "B", "B", "B", "R", "R", "V", "V", "V"],
    ["W", "B", "B", "V", "B", "B", "B", "B", "V", "V"],
    ["W", "B", "B", "V", "V", "V", "V", "V", "V", "V"]
]

expected3 = [
    ["Y", "Y", "Y", "G", "G", "G", "G", "G", "G", "G"],
    ["Y", "Y", "Y", "Y", "Y", "Y", "G", "O", "O", "O"],
    ["G", "G", "G", "G", "G", "G", "G", "O", "O", "O"],
    ["W", "W", "W", "W", "W", "G", "G", "G", "G", "O"],
    ["W", "R", "R", "R", "R", "R", "G", "O", "O", "O"],
    ["W", "W", "W", "R", "R", "G", "G", "O", "O", "O"],
    ["W", "B", "W", "R", "R", "R", "R", "R", "R", "O"],
    ["W", "B", "B", "B", "B", "R", "R", "O", "O", "O"],
    ["W", "B", "B", "O", "B", "B", "B", "B", "O", "O"],
    ["W", "B", "B", "O", "O", "O", "O", "O", "O", "O"]
]

def get_neighbors(matrix,source):
    directions = [(-1,0),(0,1),(1,1),(0,-1),(1,0)]
    row,col = source
    source_color = matrix[row][col] 
    neighbors = []

    for dy,dx in directions:
        cur_row = row + dy
        cur_col = col + dx

        if 0 <= cur_row < len(matrix) and 0 <= cur_col < len(matrix[0]) and source_color == matrix[cur_row][cur_col]:
            neighbors.append((cur_row,cur_col))
    return neighbors

def flood_fill(matrix, source, replacement_color):
    visited = set()
    path = []

    def dfs(source):
        for u in get_neighbors(matrix, source):
            if u not in visited:
                visited.add(u)
                path.append(u)
                dfs(u)

    dfs(source)

    for u in path:
        row,col = u
        matrix[row][col] = replacement_color
    
    return matrix

tests = [
    (grid1,(0,0),'O',expected1),
    (grid2,(0,0),'P',expected2),
    (grid3,(2,8),'O',expected3)
]

for i, (grid,source,rc,expected) in enumerate(tests,1):
    for m in grid: print(f"{m}")
    print('\n--')
    test = flood_fill(grid,source,rc)
    for m in test: print(f"{m}")
    assert test == expected, f"{test}, expected {expected}"
    print(f"passed: test {i}")
