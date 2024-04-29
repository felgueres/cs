# https://cses.fi/problemset/task/2165 
import sys
n = int(sys.stdin.readline())

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(source, target)
        return 1
    else:
        moves = 0
        moves += tower_of_hanoi(n-1, source, auxiliary, target)
        print(source, target)
        moves += 1
        moves += tower_of_hanoi(n-1, auxiliary, target, source)
        return moves
    
print(2**n-1)
tower_of_hanoi(n,1,3,2)