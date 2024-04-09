# https://cses.fi/problemset/task/1194
# T1: needs debugging, try solving with 2 bfs keeping track of the time it took a monster to arrive to every cell vs. player 

import sys
rows, cols = map(int, sys.stdin.readline().split())
mat = []
for _ in range(rows):
    row = list(sys.stdin.readline().strip())
    mat.append(row)

# Get monsters and start point
monsters = []
start = None
for i in range(rows):
    for j in range(cols):
        val = mat[i][j]
        if val == 'M':
            monsters.append((i,j))
        elif val == 'A':
            start = (i,j)

directions = [(-1,0,'U'),(0,1,'R'),(1,0,'D'),(0,-1,'L')]

from collections import deque

queue = deque([(start, [], monsters)])
visited = set()

def get_moves(r,c,rows,cols,monsters):
    moves = []
    for dy,dx,d_type in directions:
        rn,cn = r + dy, c + dx
        if (rn,cn) in monsters:
            continue
        if 0 <= rn < rows and 0<= cn < cols and mat[rn][cn] != '#':
            moves.append(((rn,cn),d_type))
    return moves

def is_boundary(r,c,rows,cols):
    return r == rows-1 or r == 0 or c == 0 or c == cols-1

def update_monster_moves(monsters,rows,cols):
    moves = []
    for r_m, c_m in monsters:
        for dy,dx,_ in directions:
            rn,cn = r_m + dy, c_m + dx
            if 0 <= rn < rows and 0<= cn < cols and mat[rn][cn] != '#':
                moves.append((rn,cn))
    return moves

is_found = False
while queue:
    node,path,monsters = queue.popleft() 
    r,c = node

    if is_boundary(r,c,rows,cols):
        print('YES')
        print(len(path))
        print(''.join(path))
        is_found = True 
        break
    
    if (r,c) in monsters:
        print('NO')
        break

    monster_moves = update_monster_moves(monsters,rows,cols)

    for neig,move_type in get_moves(r,c,rows,cols, monster_moves):
        if neig not in visited:
            queue.append((neig,path+[move_type],monster_moves))
            visited.add(neig)

if not is_found:
    print('NO')