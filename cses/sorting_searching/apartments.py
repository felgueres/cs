# https://cses.fi/problemset/task/1084
# classical two pointer

import sys
n, m, k = map(int, sys.stdin.readline().split())
applicants = sorted(map(int, sys.stdin.readline().strip().split()))
apartments = sorted(map(int, sys.stdin.readline().strip().split()))

i = 0  # applicants pointer 
j = 0  # apts pointer 
alloc = 0

while i < n and j < m:
    if apartments[j] < applicants[i] - k:
        j += 1
    elif apartments[j] > applicants[i] + k:
        i += 1
    else:
        alloc += 1
        i += 1
        j += 1

print(alloc)