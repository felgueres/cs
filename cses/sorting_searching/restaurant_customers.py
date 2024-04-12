# https://cses.fi/problemset/task/1619
# interval problem or interval scheduling maximiZation
# find max number of overlapping intervals 
# sweep line algorithm 
# fails one test case on speed, not correctness

import sys
n=int(sys.stdin.readline())
events=[]
for i in range(n):
    s,e=map(int,sys.stdin.readline().strip().split())
    events.append((s,'start'))
    events.append((e,'end'))

events.sort(key=lambda x:(x[0], x[1]== 'start')) #sort and prioritie by start time

max_overlaps=0
cur_overlaps=0
for e in events:
    if e[1]=='start':
        cur_overlaps+=1
        max_overlaps=max(max_overlaps,cur_overlaps)
    else:
        cur_overlaps-=1

print(max_overlaps)