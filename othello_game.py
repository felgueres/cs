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
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['W', 'B', '.', '.', '.', '.', '.', '.'],
    ['B', '.', 'W', 'B', 'B', '.', '.', '.'],
    ['B', '.', 'B', 'W', '.', '.', '.', '.'],
    ['B', 'W', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
]

tests = [((2,5),'W', True),
         ((3,4),'B', True),
         ((0,0),'W', False),
         ((2,5),'B', False),
         ((2,5),'B', False),
         ((1,2),'B', True),
         ((5,0),'W', True),
         ((4,4),'B', True),
         ((1,4),'W', True)
         ]

target = (2,1)
WHITE = 'W'
BLACK = 'B'
EMPTY = '.'

def check_valid_move_base(board, target, color):
    # Base case is to go right and check if there are sequecnes
    r,c = target

    if target == board[r][c]:
        return False
    
    opposite = BLACK if color == WHITE else WHITE 
    
    cur_col = c 
    sequence = [color]

    while cur_col < 8:
        cur_col += 1
        if board[r][cur_col] == EMPTY:
            break
        sequence.append(board[r][cur_col])
    
    if all(s == opposite for s in sequence[1:-1]) and len(sequence) >= 3 and sequence[0] == color and sequence[-1] == color:
        return sequence, True
    
    return sequence, False


def check_valid_move(board, move, color):
    # Improves on the base by adding all directions

    row,col = move

    if EMPTY != board[row][col]:
        return False

    opposite = BLACK if color == WHITE else WHITE 

    directions = [(0,1), (1,0), (-1,1), (1,-1), (1,1)]

    for dy, dx in directions:

        for direction in [1,-1]:
            sequence = [color]
            cur_row = row
            cur_col = col

            while 0 <= cur_col < 8 and 0<= cur_row<8:
                cur_row += direction * dy
                cur_col += direction * dx
                if board[cur_row][cur_col] == EMPTY:
                    break
                sequence.append(board[cur_row][cur_col])
        
            if all(s == opposite for s in sequence[1:-1]) and len(sequence) >= 3 and sequence[0] == color and sequence[-1] == color:
                return sequence, True
    
    return sequence, False

for test in tests:
    try: 
        res = check_valid_move(board, test[0], test[1])
        assert res[1] == test[2], f"Expected: {test} vs. Output: {res}"
        print(f"Passed: {test} with: {res[0]}")
    
    except AssertionError as e:
        print(e)