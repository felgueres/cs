# https://cses.fi/problemset/task/1073
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().strip().split()))

# check the top of the stack, if top < new_val, insert, else create tower
# this solution works but runs on n 
# we can do log n
# <start of first solution>
# stacks=[arr[0]]
# for num in arr[1:]:
#     found=False
#     for i,stack in enumerate(stacks):
#         if stack > num:
#             stacks[i]=num
#             found=True
#             break
#     if not found:
#         stacks.append(num)
# print(len(stacks))
# <end of first solution>

import bisect
tops = []
for num in arr:
    pos = bisect.bisect_right(tops,num) # this is the improvement, basically keeps the stack tops sorted and lets you search 
    if pos < len(tops):
        tops[pos]=num
    else:
        tops.append(num)
print(len(tops))
