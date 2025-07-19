# Given an M × N matrix of characters, find the length of the longest path in the matrix starting from a given character. 
# All characters in the longest path should be increasing and consecutive to each other in alphabetical order.
# We are allowed to search the string in all eight possible directions, i.e., North, West, South, East, North-East, North-West, South-East, South-West.

mat = [
    ['I', 'E', 'H', 'X', 'B'],
    ['A', 'H', 'G', 'P', 'E'],
    ['D', 'D', 'C', 'F', 'D'],
    ['E', 'B', 'E', 'A', 'S'],
    ['C', 'D', 'Y', 'E', 'N']
]

expected = [(2,2),(2,1),(3,2),(2,3),(1,2),(0,2)] # C, D, E, F, G, H
char = 'C'

def find_longest_path(mat, char):
    rows = len(mat)
    cols = len(mat[0])
    visited = set()
    longest_path = [] 

    def find_neighbors(mat,source):
        directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        r,c = source
        char = mat[r][c]
        target_char = chr(ord(char)+1)
        neighbors=[] 
        for dy,dx in directions:
            new_r = r + dy
            new_c = c + dx
            if 0 <= new_r < rows and 0<= new_c < cols and mat[new_r][new_c] == target_char:
                print(f'matching target char: {target_char}, {(new_r, new_c)}')
                neighbors.append((new_r,new_c))
        return neighbors

    def dfs(source, path):
        nonlocal longest_path
        if len(longest_path) < len(path): longest_path = path.copy()
        r,c = source
        visited.add(mat[r][c])
        for neighbor in find_neighbors(mat, source):
            n_r,n_c = neighbor
            if mat[n_r][n_c] not in visited:
                visited.add(mat[n_r][n_c])
                path.append(neighbor)
                dfs(neighbor, path)
                pos=path.pop()
                r,c=pos
                char = mat[r][c]
                visited.remove(char)

    paths = []
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 'C':
                path = [(r,c)]
                dfs((r,c),path)
                paths.append(path)
    
    return longest_path 

paths = find_longest_path(mat, char)
print(paths)