# Added A* flag to speed up but not passing for all
# Needs C++ 

import sys
import heapq

rows,cols = map(int,sys.stdin.readline().split())
mat = []
for i in range(rows): 
    mat.append(list(sys.stdin.readline().strip()))

src = None
dest = None

for i in range(rows):
    for j in range(cols):
        if mat[i][j] == 'A':
            src = (i,j)
        elif mat[i][j] == 'B':
            dest = (i, j)
use_a_star = True if rows*cols>100000 else False

if not src:
    print('NO')
    sys.exit()

def manhattan_distance(src,dest):
    return abs(src[0] - dest[0]) + abs(src[1] - dest[1])

if use_a_star:
    queue = [([0+manhattan_distance(src,dest),src,[]])]
else:
    from collections import deque
    queue = deque([(src,[])])

found = False
sol_path = None
dirs = [(-1,0,'U'),(0,1,'R'),(1,0,'D'),(0,-1,'L')]
visited = set([src])

while queue and not found:
    if use_a_star:
        _, (r,c),path = heapq.heappop(queue)
    else:
        (r,c),path = queue.popleft()

    if (r,c) == dest:
        print('YES')
        print(len(path))
        print(''.join(path))
        break

    for dy,dx,move_type in dirs:
        rn,cn=r+dy,c+dx
        if 0 <= rn < rows and 0<=cn<cols and mat[rn][cn] not in ('#','V'):
            visited.add((rn,cn))
            new_path = path + [move_type]
            if use_a_star:
                priority = len(new_path) + manhattan_distance((rn,cn), dest)
                heapq.heappush(queue, (priority,(rn,cn),new_path))
            else:
                queue.append(((rn,cn),new_path))
else:
    print('NO')
