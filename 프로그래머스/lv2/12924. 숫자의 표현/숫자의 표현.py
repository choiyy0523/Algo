# 특정 숫자부터 시작하는 연속된 자연수의 합이 n이 되는지 판단하는 함수
def checksum(n, start):
    plus = start
    total = 0
    while total < n:
        total += plus
        plus += 1
    if total == n:
        return True
    else:
        return False
    
def solution(n):
    cnt = 0
    start = 1
    while start <= n:
        if checksum(n, start):
            cnt += 1
        start += 1
    return cnt

print(solution(15))