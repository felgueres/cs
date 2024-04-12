# https://cses.fi/problemset/task/1069
# A,C,G,T
# find max substring of only one type of char
import sys
chars = sys.stdin.readline()
max_cnt=0
cur_cnt=0
last_char=chars[0]
for ch in chars:
    if ch == last_char:
        cur_cnt+=1
        if cur_cnt>max_cnt:
            max_cnt=cur_cnt
    else:
        cur_cnt=1
    last_char=ch
print(max_cnt)
