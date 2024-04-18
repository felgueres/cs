# https://cses.fi/problemset/task/2163
# nested ranges check
# sort and sweep technique

import sys
n=int(sys.stdin.readline())
ranges=[]
for i in range(n):
    x,y=list(map(int, sys.stdin.readline().strip().split()))
    ranges.append((x,y,i))

# Contains array
contains = [0] * len(ranges)
is_contained = [0] * len(ranges)

# Sort by start, then by end descending
# Sweep for containment
ranges.sort(key=lambda r: (r[0], -r[1]))
max_end = 0
for x, y, i in ranges:
    if max_end >= y:
        is_contained[i] = 1
    max_end = max(max_end, y)

# TODO: Sweep again to figure out if range contains other ranges
