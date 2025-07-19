'''
Given an `M × N` matrix of integers whose each cell can contain a negative, zero, or a positive value, 
determine the minimum number of passes required to convert all negative values in the matrix positive.

Only a non-zero positive value at cell (i, j) can convert negative values present at its adjacent cells (i-1, j), (i+1, j), (i, j-1), and (i, j+1)
i.e., up, down, left and right.

Input:
mat = [
	[-1, -9,  0, -1,  0],
	[-8, -3, -2,  9, -7],
	[ 2,  0,  0, -6,  0],
	[ 0, -7, -3,  5, -4]
]
Output: 3
'''

# Do the first pass 
mat = [
	[-1, -9,  0, -1,  0],
	[-8, -3, -2,  9, -7],
	[ 2,  0,  0, -6,  0],
	[ 0, -7, -3,  5, -4]
]

def get_positive_nums(mat):
    nums = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]>0:
                nums.append((i,j))
    return nums

def get_neighbors(mat, source):
    neighbors = []
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    for dy,dx in directions:
        cur_r = source[0]+dy
        cur_c = source[1]+dx
        if 0 <= cur_r < len(mat) and 0<= cur_c < len(mat[0]) and mat[cur_r][cur_c] <0:
            neighbors.append((cur_r, cur_c))
    return neighbors

from collections import deque

cnt_passes = 0
new_queue = deque()

while True:
    queue = deque(get_positive_nums(mat))
    is_change = False
    while queue:
        cur = queue.popleft()
        neighbors = get_neighbors(mat, cur)
        for neighbor in neighbors:
            mat[neighbor[0]][neighbor[1]]= mat[neighbor[0]][neighbor[1]] * -1
            is_change = True
    if not is_change:
        break
    cnt_passes+=1

for r in mat: 
    print(r)

print(f"Took {cnt_passes}")