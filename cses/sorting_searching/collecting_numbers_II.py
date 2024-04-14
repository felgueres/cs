# https://cses.fi/problemset/task/2217 
# arr contains 1 ... n exactly once
# swapping indeces
import sys
n,m=map(int,sys.stdin.readline().split())
lst=list(map(int,sys.stdin.readline().strip().split()))
ix_arr=[]

for i in range(m):
    i1,i2=map(int,sys.stdin.readline().strip().split())
    ix_arr.append((i1-1,i2-1))

def swap(lst,i1,i2,num_dict):
    lst[i1],lst[i2] = lst[i2],lst[i1]
    num_dict[lst[i1]],num_dict[lst[i2]] = i1,i2
    return lst,num_dict

num_dict = {x:i for i,x in enumerate(lst)}

for i1,i2 in ix_arr:
    lst,num_dict = swap(lst,i1,i2,num_dict)
    rounds=1
    cur=0

    for j in range(1,n+1):
        if num_dict[j]<cur:
            rounds+=1
        cur = num_dict[j]

    print(rounds)