#import sys

#sys.stdin = open('input.txt')

#A, B, C = map(int, sys.stdin.readline().split())
#parking_info = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

# 매번 이런 유형의 문제를 볼 때마다 큐라고 생각해서 괜히 어렵게 푸는 것 같다...
# 물론 실제로 큐로 풀어야하는 경우도 있긴 한데, 어떤 경우인지 잘 판단할 필요가 있음
# https://school.programmers.co.kr/learn/courses/30/lessons/42586 기능개발 -> 스택/큐

A, B, C = map(int, input().split())
parking_info = [list(map(int, input().split())) for _ in range(3)]

timeline = [0] * 100

for info in parking_info:
    for i in range(info[0], info[1]):
        timeline[i] += 1

fare = 0
for i in timeline:
    if i == 1:
        fare += A
    elif i == 2:
        fare += 2*B
    elif i == 3:
        fare += 3*C

print(fare)