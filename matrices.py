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
import numpy as np
import argparse

def board(r,c):
    '''
    Returns a zero-value r x c board.
    A matrix of r x c has r elements with c sub-elements.
    '''
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append('.')
        matrix.append(row)
    return matrix


def change_element(board,r,c,e):
    '''
    i and j are index of element to change.
    e is the new element.
    zero-indexed board.
    '''
    board[r][c] = e
    return board

def pprint(board):
    for r in board:
        print(r)
    print('\n')

def check_goodline_endpoint(board, rMove, cMove, color):
    # Check row / horizontal
    # Check col / vertical 
    # Check diagonal
    # Break if any

    # Approach: 
    # 1. Isolate the row
    # 2. Check if there is a good line
    # 3. Isolate the good line
    # 4. Check if the move is an end to the good line
    pass

if __name__ == '__main__':
    # Plan:
    # validate board 
    # create temp board
    # change with the potential move
    # evaluate is_move_valid
    # fix edge cases 

    colors = ['B','W']

    board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]]
 
    rMove = 4
    cMove = 3
    color = 'B'

    # board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]]

    # rMove = 4
    # cMove = 4
    # color = "W"

    print('original board')
    pprint(board)

    _board = change_element(board,rMove,cMove,color)
    print('attempt move')
    print(f'rMove:{rMove}, cMove{cMove}')
    pprint(_board)


    def get_opposite_color(color):
        return 'W' if color == 'B' else 'B'

    def is_good_line(li):
        first = li[0] 
        if first not in colors:
            return False
        current_line = ['sol']
        for e in li[1:]:            
            if e not in colors:
                return 0 

            elif e != first: 
                current_line.append(e)

            else: 
                current_line.append('eol')
                break

        if len(current_line)>=3 and current_line[-1]=='eol':
            return len(current_line)

        return 0

    rEndpoints = [] 
    _row = _board[rMove]
    for i,e in enumerate(_row):
        flag = is_good_line(_row[i:])
        if flag > 0:
            rEndpoints.extend([i,i+flag-1])

    cEndpoints = []
    _col = [row[cMove] for row in _board]
    for i,e in enumerate(_col):
        flag = is_good_line(_col[i:])
        if flag > 0:
            cEndpoints.extend([i,i+flag-1])

    dEndpoints = []
    def getDiagonalsStarts(board, rMove, cMove):
        first = []
        r1 = rMove
        c1 = cMove
        while r1 > 0 and c1 > 0:
            r1 -=1
            c1 -=1
        r2 = rMove
        c2 = cMove

        while r2 < 7 and c2 > 0:
            r2 +=1
            c2 -=1
        return [(r1,c2),(r2,c2)]

    def getDiagonals(board, start_pos):
        d1,d2 = start_pos[0],start_pos[1] 
        print('starts')
        print(f'd1 starts {d1}')
        print(f'd2 starts {d2}')

        r1,c1 = d1
        diagonal1 = []
        while r1<=7:
            diagonal1.append(board[r1][c1])
            r1 += 1
            c1 += 1

        r2,c2 = d2
        diagonal2 = []
        while r2>=0 and c2 <=7:
            diagonal2.append(board[r2][c2])
            r2 -= 1
            c2 += 1

        print(f'Diagonal1: {diagonal1}')
        print(f'Diagonal2: {diagonal2}')

    if cMove in rEndpoints or rMove in cEndpoints:
        print(True)
    else:
        print(False)

    start_pos = getDiagonalsStarts(board,rMove,cMove)
    getDiagonals(board,start_pos)


