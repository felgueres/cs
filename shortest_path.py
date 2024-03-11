# You are planning a science expedition, and you need to pick a base camp location.  
# The environment has open spaces (' ') and impassable mountains ('#').  
# There are several points of interest ('P') that need to be explored.  
# Each exploration takes an entire day (neglect travel time), and the 
# science team must return to camp each night after exploring a point of interest.  
# Fuel is expensive so you need to minimize total distance traveled.  What is the best location for the base camp?
# grid = [
#      0   1 . 2 . 3   4 . 5 . 6 . 7 . 8
#  0 ['#','#','#','#','#','#','#','#','#'],
#  1 ['#','P','#',' ',' ','#','#',' ','#'],
#  2 ['#',' ',' ','#',' ','#','#',' ','#'],
#  3 ['#',' ',' ','#',' ',' ','#',' ','#'],
#  4 ['#',' ',' ',' ','#',' ','#',' ','#'],
#  5 ['#',' ',' ',' ',' ',' ',' ',' ','#'],
#  6 ['#',' ','P',' ',' ','#','#','#','#'],
#  7 ['#','#','#','#','#','#','#','#','#']
# ]

grid = [
  ['#','#','#','#','#','#','#','#','#'],
  ['#','P','#',' ',' ','#','#',' ','#'],
  ['#',' ',' ','#',' ','#','#',' ','#'],
  ['#',' ',' ','#',' ',' ','#',' ','#'],
  ['#',' ',' ',' ','#',' ','#',' ','#'],
  ['#',' ',' ',' ',' ',' ',' ',' ','#'],
  ['#',' ','P',' ',' ','#','#','#','#'],
  ['#','#','#','#','#','#','#','#','#']
]

def get_neighbors(u, grid):
    x,y = u
    #             up,   right, down, left 
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    neighbors = []
    for (dx,dy) in directions:
        cur_x = x+dx
        cur_y = y+dy
        if 0 <= x < len(grid)-1 and 0<= y < len(grid[0])-1 and grid[cur_x][cur_y] != '#':
            neighbors.append((cur_x, cur_y))
    return neighbors

def bfs_from_source(source, grid):
    queue = [(source, 0)]
    visited = set()
    paths = []

    while queue:
        u, distance = queue.pop(0)
        for neighbor in get_neighbors(u, grid):
            if neighbor not in visited:
                row,col = neighbor
                if grid[row][col] == 'P':
                    paths.append(((row,col), distance+1))
                queue.append((neighbor, distance+1))
                visited.add(neighbor)
    return paths

# MIN DISTANCE TO TARGETS FROM SINGLE SOURCE 
sources_with_distances = {} 
try:
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cur_source = row,col
            if grid[row][col] not in ['P', '#']:
                paths = bfs_from_source(source=cur_source, grid=grid)
                distance = sum([distance for (_, distance) in paths]) 
                sources_with_distances[(row,col)] = distance
except Exception as e:
    print(e) 

[print(f"{x[0]} with distance: {x[1]}") for x in sorted(sources_with_distances.items(), key=lambda item: item[1])]

# TESTING THE BFS FUNCTION
# tests -> (input, [(target, distance)], total_distance)
# bfs_tests = [((2,1), [((1,1),1), ((6,2),5)], 6),
#              ((3,2), [((1,1),3), ((6,2),3)], 6)]

# for test in bfs_tests:
#     source = test[0]
#     paths_to_targets = bfs_from_source(source=source, grid=grid)
#     print('found paths ->', paths_to_targets)
#     total_distance = sum([distance for (_, distance) in paths_to_targets]) 
#     assert total_distance == test[2], f"wrong answer {total_distance} expected {test[2]}"
#     print(f'passed test -> {test}')

# TESTING NEIGHBOR FUNCTION
# neighbor_tests = [((3,1), [(2,1), (3,2), (4,1)])]
# for test,expected  in neighbor_tests:
#     neighbors = set(get_neighbors(test, grid))
#     assert set(expected) == set(neighbors)
#     print(f"Exp: {expected} vs. Actual: {neighbors}")