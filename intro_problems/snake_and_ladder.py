"""
Given a 10 x 10 board of snake and ladder game, marked with numbers in the range [1-100], 
find the minimum number of throws required to win it (reach board #1 to board #100).

Input: Dictionary of snakes and ladders

Ladder = {80=99, 1=38, 51=67, 4=14, 21=42, 72=91, 9=31, 28=84}
Snake = {64=60, 17=7, 98=79, 54=34, 87=36, 93=73, 62=19, 95=75}

board = [
    [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [80, 79, 78, 77, 76, 75, 74, 73, 72, 71],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [60, 59, 58, 57, 56, 55, 54, 53, 52, 51],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [40, 39, 38, 37, 36, 35, 34, 33, 32, 31],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
]

Output: 7

"""
from collections import deque

def find_min_moves():
    ladder = {80: 99, 1: 38, 51: 67, 4: 14, 21: 42, 72: 91, 9: 31, 28: 84}
    snake = {64: 60, 17: 7, 98: 79, 54: 34, 87: 36, 93: 73, 62: 19, 95: 75}
    board_size = 10 * 10 
    nums = range(1,board_size+1)
    # create an edge list
    # for every number, create an edge to number + 1 .. 6
    # check ladders and snakes and replace their corresponding value 
    edges = []
    for num in nums: # n * 6
        for i in range(1,7): 
            cur_dest = num + i
            if cur_dest in ladder:
                edges.append((num, ladder[cur_dest]))
            elif cur_dest in snake:
                edges.append((num, snake[cur_dest]))
            elif cur_dest <= 100:
                edges.append((num, num+i))
            else:
                break
    
    # shortest path  
    adj_list = {k:[] for k in nums}
    for (u,v) in edges: adj_list[u].append(v)
    src = 1

    Q = deque([(src,0)])
    visited = set()

    while Q:
        node,step = Q.popleft()

        if node == 100:
            return step

        for neighbor in adj_list.get(node,[]):
            if neighbor not in visited:
                Q.append((neighbor, step+1))
                visited.add(neighbor)
    
    return -1 

print(find_min_moves())