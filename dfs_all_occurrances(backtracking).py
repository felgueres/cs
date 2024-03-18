# Given an M × N matrix of characters, find all occurrences of a given string in the matrix. 
# We are allowed to search the string in all eight possible directions, 
# i.e., North, West, South, East, North-East, North-West, South-East, South-West. 
# Note that there should not be any cycles in the output path.

# This problem requires backtracking to track all possible solutions!

mat = [
    ["D", "E", "M", "X", "B"],
    ["A", "O", "E", "P", "E"],
    ["D", "D", "C", "O", "D"],
    ["E", "B", "E", "D", "S"],
    ["C", "P", "Y", "E", "N"]
]

word = "CODE"

def find_neighbors(mat,s):
    directions = [(-1,0),(1,1),(0,1),(1,0),(1,-1),(0,-1),(-1,1),(-1,-1)]
    row,col = s
    char = mat[s[0]][s[1]]
    next_char = word.index(char) + 1 if word.index(char) + 1 < len(word) else None

    if next_char is None: return []

    neighbors = []

    for dy,dx in directions:
        crow = row + dy
        ccol = col + dx
        if 0 <= crow < len(mat) and 0 <= ccol < len(mat[0]) and mat[crow][ccol] == word[next_char]:
            neighbors.append((crow,ccol))
    return neighbors

def find_occurences(mat, word):
    f_chars = [(m,n) for m in range(len(mat)) for n in range(len(mat[0])) if mat[m][n] == word[0]]
    sequences = []

    def dfs(s, path, index):

        if index == len(word):
            sequences.append(path[:])

        neighbors = find_neighbors(mat,s)

        for n in neighbors:
            if n not in path:
                path.append(n)
                dfs(n, path, index+1)
                path.pop() # this is the crucial piece for backtracking, it pops the last element when there are no more neighbors

    for f_char in f_chars:
        dfs(f_char,[f_char],1)

    return sequences

print(find_occurences(mat,word))