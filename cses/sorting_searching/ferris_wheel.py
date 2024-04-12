# https://cses.fi/problemset/task/1090

import sys
n, max_weight = map(int, sys.stdin.readline().split())
weights = sorted(map(int, sys.stdin.readline().strip().split()))

i, j = 0, n - 1
gondolas = 0
while i <= j:
    if weights[i] + weights[j] <= max_weight:
        i += 1
    j -= 1 
    gondolas += 1

print(gondolas)