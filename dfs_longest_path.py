# Given an M × N matrix of characters, find the length of the longest path in the matrix starting from a given character. 
# All characters in the longest path should be increasing and consecutive to each other in alphabetical order.
# We are allowed to search the string in all eight possible directions, i.e., North, West, South, East, North-East, North-West, South-East, South-West.

grid1 = [
    ['D', 'E', 'H', 'X', 'B'],
    ['A', 'O', 'G', 'P', 'E'],
    ['D', 'D', 'C', 'F', 'D'],
    ['E', 'B', 'E', 'A', 'S'],
    ['C', 'D', 'Y', 'E', 'N']
]
expected1 = [(2,2),(2,1),(3,2),(2,3),(1,2),(0,2)] # C, D, E, F, G, H
char1 = 'C'

# This can be solved by either bfs or dfs 
# The complexity of these is O(V+E) per algo run
# Meaning that if you have n instances of character, complexity would be O(V+E * n)

def find_neighbors(grid, position):
    directions = [(-1,0),(1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1),(-1,-1)]
    row,col = position
    neighbors = []

    for dy,dx in directions:
        cur_row = row + dy
        cur_col = col + dx
        if 0 <= cur_row < len(grid) and 0 <= cur_col < len(grid[0]):
            last_char = grid[row][col]
            cur_char = grid[cur_row][cur_col]
            next_char = chr(ord(last_char) + 1)
            if cur_char == next_char: # should be only one char up
                neighbors.append((cur_row,cur_col))
    return neighbors

def find_chars(grid, char):
    chars = []
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == char:
                chars.append((m,n))
    return chars

def find_longest_path(grid, char):
    visited = set()
    paths = []

    def dfs(source, path):
        visited.add(source)
        for n in find_neighbors(grid, source):
            if n not in visited:
                dfs(n, path + [n])
        paths.append(path)
    
    for c in find_chars(grid,char):
        if c not in visited:
            dfs(c, [c])
    
    longest_path = []
    for path in paths:
        if len(path) > len(longest_path):
            longest_path = path

    return longest_path
            
print(find_longest_path(grid1, char1))