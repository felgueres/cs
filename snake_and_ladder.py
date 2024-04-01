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
Explanation: The game requires at least 7 dice throws to win.

Doing this problem by manipulating the matrix is complicated.
Better to reprent the matrix as an adj list. 
Find the shortest path between 1 and 100.
This is a great problem because shows resourcefulness, skill, and tests graph understanding.

"""


ladder = {80: 99, 1: 38, 51: 67, 4: 14, 21: 42, 72: 91, 9: 31, 28: 84}
snake = {64: 60, 17: 7, 98: 79, 54: 34, 87: 36, 93: 73, 62: 19, 95: 75}

# create edge list
n = 10 * 10 
edges = []
for i in range(1,n+1):
    j = 1
    while j <= 6 and i + j <= n:
        source = i
        dest = i + j
        cur_ladder = ladder.get(dest, 0)
        cur_snake = snake.get(dest,0)
        if cur_snake > 0 or cur_ladder > 0: dest = cur_ladder + cur_snake
        edges.append((source,dest))
        j += 1

from collections import deque

def find_min_moves(edges, source=1, destination=100):
    adj_list = { k : [] for k in range(source,destination+1) }
    for (s,d) in edges: adj_list[s].append(d)
    queue = deque([(source, 0)])
    visited = set((source))
    while queue:
        source, moves = queue.popleft()
        print(f"{source}, {moves}")
        for neighbor in adj_list.get(source):
            if neighbor not in visited:
                if neighbor == destination:
                    return moves+1 
                queue.append((neighbor, moves+1))
                visited.add(neighbor)
    return -1

min_moves = find_min_moves(edges)
print(f"Min moves: {min_moves}")

# Runs on O(V+E), V from looping to initialize each Vertex and E from visiting the edges 