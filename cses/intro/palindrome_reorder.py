# https://cses.fi/problemset/task/1755
import sys
input_str=sys.stdin.readline().strip()
l = list(input_str)
from collections import defaultdict
d = defaultdict(int)
for ch in l: 
    d[ch]+=1

odd=0
first = []
second = []
mid = []
for ch, cnt in sorted(d.items()):
    if cnt % 2 != 0:
        odd+=1
        if odd > 1:
            print("NO SOLUTION")
            exit(0)
        mid.append(ch*(cnt%2))
    first.append(ch*(cnt//2))
    second.append(ch*(cnt//2))

second.reverse()
print(''.join(first+mid+second))