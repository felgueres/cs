board = [
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','W','.','.','.','.','.'],
    ['.','B','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.']
]

def is_valid(board, start, end):
    rows = len(board)
    cols = len(board[0])
    r,c = start    
    directions=[(-1,1),(-1,-1)]
    color = board[r][c]
    opposite_color = 'W' if color == 'B' else 'B'
    for dy,dx in directions:
        rn,rc = r+dy,c+dx
        if 0<=rn<rows and 0<=rc<cols:
            cur = board[rn][rc]
            if cur == '.':
                return True
            else:
                return False
    return False

start=(6,2)
end=(4,3)


