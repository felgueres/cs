# https://cses.fi/problemset/task/1092

import sys
n = int(sys.stdin.readline())
def sum_of_natural(n):
    return (n*(n+1))/2

if sum_of_natural(n) %2 !=0:
    print('NO')
    exit(0)


set1,set2 = [],[]
set1_sum,set2_sum = 0,0

for number in range(n,0,-1):
    if set1_sum <= set2_sum:
        set1.append(number)
        set1_sum += number
    else:
        set2.append(number)
        set2_sum += number
    
print('YES')
print(len(set1))
print(' '.join(map(str,set1)))
print(len(set2))
print(' '.join(map(str,set2)))