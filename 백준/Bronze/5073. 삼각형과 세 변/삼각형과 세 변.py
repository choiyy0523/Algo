import sys

# sys.stdin = open('input.txt')

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a==0 and b==0 and c==0:
        break
    else:
        # 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid"
        if max(a, b, c) >= sum([a, b, c]) - max(a, b, c):
            print("Invalid")

        else:
            # Equilateral :  세 변의 길이가 모두 같은 경우
            if len(set([a, b, c])) == 1:
                print("Equilateral")
            # Isosceles : 두 변의 길이만 같은 경우
            elif len(set([a, b, c])) == 2:
                print("Isosceles")
            # Scalene : 세 변의 길이가 모두 다른 경우
            else:
                print("Scalene")