# Given an M × N boggle board, find a list of all possible words that can be formed by a sequence of adjacent characters on the board.
# We are allowed to search a word in all eight possible directions, i.e., North, West, South, East, North-East, North-West, South-East, South-West, but a word should not have multiple instances of the same cell.
# Consider the following the traditional 4 × 4 boggle board. If the input dictionary is [START, NOTE, SAND, STONED], the valid words are [NOTE, SAND, STONED].

board = [
    ['M','S','E','F'],
    ['R','A','T','D'],
    ['L','O','N','E'],
    ['K','A','F','B']
]

input1 = ['START','NOTE','SAND','STONED']
output1 = ['NOTE','SAND','STONED']

input2 = ['NOTA','RAT','SEAT','FEAST','PABLO','MRSAX']
output2 = ['NOTA','RAT','SEAT','FEAST']

tests = [
    (input1, output1),
    (input2, output2)
]

def find_words(board, words):
    # for word, find first character in board
    # recurse to find path of word
    # # move 8 ways next character 
    # if one path, return it
    # not global state for visited nodes because you'll be trying each word
    # improvements: keep dictionary of characters, to avoid searching if not in board

    found = []

    def find_neighbors(s,word,index) -> list:
        directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        row,col = s
        neighbors = []
        next_char = word[index] if index < len(word) else None
        if next_char is None: return []
        for dy,dx in directions:
            cur_row = row+dy
            cur_col = col+dx
            if 0 <= cur_row < len(board) and 0 <= cur_col < len(board[0]) and board[cur_row][cur_col] == next_char:
                neighbors.append((cur_row,cur_col))
        return neighbors

    def dfs(s,path,index,word):
        if word in found:
            return 

        if index == len(word):
            print(f'found word!, {path}, {word}')
            found.append((word))

        for neighbor in find_neighbors(s,word,index):
            if neighbor not in path:
                path.append(neighbor)
                dfs(neighbor, path, index+1, word)
                path.pop()

    for word in words:
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == word[0]:
                    dfs((m,n),[(m,n)],1,word)
    
    return found

for test in tests:
    input, output = test[0], test[1]
    eval = find_words(board,input)
    assert set(eval) == set(output), f"{eval}, expected {output}"
