# https://cses.fi/problemset/task/2205
import sys
n = int(sys.stdin.readline())

def gen_gray_code(n):
    if n == 0:
        return ["0"]
    if n == 1:
        return ["0","1"]
    previous_gray = gen_gray_code(n - 1)
    new_gray = []
    new_gray.extend('0' + code for code in previous_gray)
    new_gray.extend('1' + code for code in reversed(previous_gray))
    return new_gray

for l in gen_gray_code(n):
    print(l)