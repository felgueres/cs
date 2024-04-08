'''
You are given a 0-indexed 8 x 8 grid board, where board[r][c] represents the cell (r, c) on a game board. 
On the board, free cells are represented by '.', white cells are represented by 'W', and black cells are represented by 'B'.

Each move in this game consists of choosing a free cell and changing it to the color you are playing as (either white or black). 
However, a move is only legal if, after changing it, the cell becomes the endpoint of a good line (horizontal, vertical, or diagonal).

A good line is a line of three or more cells (including the endpoints) where the endpoints of the line are one color, and the remaining cells in the middle are the opposite color (no cells in the line are free). 

Horizontal: 
- B - W - B (Good)
- B - B - W (Bad)
- W - B - B -W (Good)
'''

board = [
    ['.', '.', '.', '.', '.', '.'],
    ['W', 'B', '.', '.', '.', '.'],
    ['B', '.', '.', 'B', 'B', 'W'],
    ['B', '.', 'B', 'W', '.', '.'],
    ['B', 'W', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
    ['B', 'W', 'W', 'W', '.', '.'],
]

tests = [((2,2), 'W', True), 
         ((3,4), 'B', True), 
         ((1,4), 'W', True),
         ((0,5), 'W', False),
         ((0,6), 'W', False),
         ((0,1), 'B', False),
         ]

def is_valid_move(board,move,color):
    direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    for (dy,dx) in direction:
        seq = [color]
        cur_row, cur_col = move[0]+dy, move[1]+dx
        while 0 <= cur_row < len(board) and 0 <= cur_col < len(board[0]) and board[cur_row][cur_col] != '.':
            seq.append(board[cur_row][cur_col])
            cur_row += dy
            cur_col += dx
        if seq[0] == color and seq[-1] == color and len(seq)>=3 and all(char!=color for char in seq[1:-1]):
            print(f'valid seq -> {seq}')
            return True
    return False
    
for t in tests:
    output = is_valid_move(board, t[0], t[1]) 
    assert output == t[2], f'{t}: {output}, expected: {t[2]}'
    print("Tests passed!")
