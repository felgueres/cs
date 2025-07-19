# Chess Knight problem
# Given a chessboard, find the shortest distance (minimum number of steps) taken by a knight 
# to reach a given destination from a given source.

n = 8
source = (7,0)
destination = (0,7)
output = 6

# method
# init board
# knight moves in L -> (1,2),(1,-2),(-1,2),(-1,-2)
# bfs to check all moves, record distance
# when found, print distance

# Notes:
# Color doesnt matter!

board = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']
] 

def get_knight_moves(board, source):
    directions = [(-2,-1),(-2,1),(-1,2),(1,2),(2,2),(2,-2),(1,-2),(-1,-2)]
    row,col = source
    moves = []
    for (dy,dx) in directions:
        cur_row = row + dy
        cur_col = col + dx
        if 0 <= cur_row < len(board) and 0 <= cur_col < len(board[0]):
            moves.append((cur_row,cur_col))
    return moves

from collections import deque 

S = [(source,0)]
queue = deque(S)
visited = set()
loop = True 
while queue and loop:
    node,distance = queue.popleft()
    for neighbor in get_knight_moves(board, node):
        print(f"{neighbor} == {destination}: {neighbor==destination}")
        if neighbor == destination:
            print(f'moves: {distance + 1}')
            loop = False
            break
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, distance+1))
