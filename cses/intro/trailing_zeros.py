# https://cses.fi/problemset/task/1618
import sys
sys.setrecursionlimit(10**7)
n = int(sys.stdin.readline())

# my answer
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# res = factorial(n)
# iter_res = iter(str(res)[::-1])
# ans=0
# while iter_res:
#     i = iter_res.__next__()
#     if i == '0':
#         ans+=1
#         continue
#     break
# print(ans)

# theres math to make this computable
# A more efficient way to count trailing zeros in a factorial is to count how many times the number 5 is a factor in the numbers from 1 to n
# each trailing zero in a factorial comes from a factor of 10

count = 0
while n>=5:
    n //=5
    count+=n
print(count)