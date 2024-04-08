import sys
from collections import deque

ROWS,COLS = map(int,sys.stdin.readline().split())

mat = []
for _ in range(ROWS): 
    mat.append(list(sys.stdin.readline().strip()))

visited = set()
DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(root):
    queue = deque([root])
    while queue:
        r,c = queue.popleft()
        for dy,dx in DIRS:
            nr,nc = r + dy, c+dx
            if 0<=nr<ROWS and 0<=nc<COLS and mat[nr][nc] == '.':
                mat[nr][nc] = 'X'
                queue.append((nr,nc))

rooms = 0
for i in range(ROWS):
    for j in range(COLS):
        if mat[i][j] == '.':
            bfs((i,j))
            rooms += 1

print(rooms)