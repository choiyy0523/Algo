# import sys

# sys.stdin = open('input.txt')

# test_str = list(sys.stdin.readline().upper())
test_str = list(input().upper())
char_list = list(set(test_str))

max_char = ''
max_cnt = 0
cnt_list = []

for c in char_list:
    cnt = 0
    for i in test_str:
        if c == i :
            cnt += 1
    cnt_list.append(cnt)
    if cnt >= max_cnt:
        max_cnt = cnt
        max_char = c

if cnt_list.count(max_cnt) != 1:
    print('?')
else:
    print(max_char)
