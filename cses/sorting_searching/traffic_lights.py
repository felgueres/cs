# https://cses.fi/problemset/task/1163

import sys
x,n=map(int, sys.stdin.readline().split())
lights=list(map(int, sys.stdin.readline().strip().split()))

# naive first attempt
pos=list(range(x+1))
passages=[]

for light in lights:
    pos[light]='x'
    cur_sum=0
    max_sum=0
    print(pos)
    for num in pos:
        if num == 'x':
            max_sum=max(cur_sum,max_sum)
            cur_sum=0
        else:
            cur_sum+=1
            max_sum=max(cur_sum,max_sum)
    passages.append(max_sum)

print(' '.join(map(str,passages)))

# this is not efficient. needs to scan O(n) list to insert new positions.
# then iterates O(n) to find max
# better solution is n log n using binary search to get position and hashmap

# todo: implement better solution
