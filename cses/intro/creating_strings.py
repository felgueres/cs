# https://cses.fi/problemset/task/1622
import sys
strings = list(sys.stdin.readline().strip())

combinations=set()

def permute(a,l,h):
    if l == h:
        combinations.add(''.join(a))
    
    for i in range(l,h):
        a[i],a[l]=a[l],a[i]
        permute(a,l+1,h)
        a[i],a[l]=a[l],a[i]

permute(strings,0,len(strings))

combinations = sorted(combinations)

print(len(combinations))
for s in combinations:
    print(s)