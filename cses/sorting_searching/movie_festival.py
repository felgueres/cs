# https://cses.fi/problemset/task/1629 
# interval problem
# find max number of non-overlapping intervals 
# sweep line algorithm 

import sys
n=int(sys.stdin.readline())
events=[]
for i in range(n):
    s,e=map(int,sys.stdin.readline().strip().split())
    events.append((s,e))

events.sort(key=lambda x:x[1])

last_end_time = -1
count = 0
for start,end in events:
    if start>=last_end_time:
        last_end_time=end 
        count+=1

print(count)