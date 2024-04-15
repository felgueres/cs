# https://cses.fi/problemset/task/1163
# range query, online algorithm

import sys
import bisect 

x,n=map(int, sys.stdin.readline().split())
lights_ixs=list(map(int, sys.stdin.readline().strip().split()))

s = [0,x]
ms = [x]
ans=[]
for light_ix in lights_ixs:
    ix= bisect.bisect_right(s,light_ix) #search where to insert new light
    left = s[ix-1] #from this point, determine previous segment size 
    right = s[ix] 
    old_s = right-left
    ms.remove(old_s) #update it
    new_left=light_ix-left
    new_right=right-light_ix #from the split, you have one new segment, and two new sizes 
    bisect.insort(ms,new_left) #insert the segment sizes in order
    bisect.insort(ms,new_right)
    ans.append(ms[-1]) # grab the last element since it's ordered is the max
    s.insert(ix,light_ix) # finally insert the ix onto segment indeces 

print(' '.join(map(str,ans)))

# naive first attempt
# pos=list(range(x+1))
# passages=[]
# 
# for light in lights:
#     pos[light]='x'
#     cur_sum=0
#     max_sum=0
#     for num in pos[1:]:
#         cur_sum+=1
#         if num == 'x':
#             max_sum=max(cur_sum,max_sum)
#             cur_sum=0
#         else:
#             max_sum=max(cur_sum,max_sum)
#     passages.append(max_sum)
# 
# print(' '.join(map(str,passages)))

