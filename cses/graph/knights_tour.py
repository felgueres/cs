# This is directionally correct but you need better heuristics to solve it in reasonable time 
# Otherwise this can go for ages

import sys
x,y = map(int, sys.stdin.readline().split())
r,c = y-1, x-1
ROWS = 8
COLS = 8

board = []
for i in range(8):
    row = [False] * 8
    board.append(row)

dirs = [(1,2),(-1,2),(1,-2),(-2,-1),(-1,-2),(2,1),(-2,1),(2,-1)]

def dfs(root,move_num):
    if move_num == 64: 
        return True
    r,c = root 
    for dy,dx in dirs:
        nr,nc = r+dy,c+dx
        if 0<=nr<ROWS and 0<=nc<COLS and not board[nr][nc]: 
            board[nr][nc] = move_num+1
            if dfs((nr,nc), move_num+1):
                return True
            board[nr][nc] = False
    return False

board[r][c] = 1
dfs((r,c),1)

for r in board: 
    print(' '.join(map(str,r)))