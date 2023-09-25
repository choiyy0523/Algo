import sys
nums = list(map(int, sys.stdin.readline().split()))

if nums == [1, 2, 3, 4, 5, 6, 7, 8]:
    answer = 'ascending'
elif nums == [8, 7, 6, 5, 4, 3, 2, 1]:
    answer = 'descending'
else:
    answer = 'mixed'

print(answer)