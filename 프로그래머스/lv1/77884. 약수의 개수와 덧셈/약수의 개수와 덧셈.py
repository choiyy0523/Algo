def divisor_odd_check(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt % 2 == 0:
        return True
    else:
        return False

def solution(left, right):
    tot = 0
    for num in range(left, right+1):
        if divisor_odd_check(num):
            tot += num
        else:
            tot -= num
    return tot