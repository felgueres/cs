import sys
n = int(sys.stdin.readline())

ans=[]

def weird_algorithm(num):
    ans.append(num)
    if num == 1:
        return num
    if num % 2 == 0:
        return weird_algorithm(num//2) 
    else:
        return weird_algorithm((num*3)+1) 

weird_algorithm(n)

print(' '.join(map(str,ans)))
