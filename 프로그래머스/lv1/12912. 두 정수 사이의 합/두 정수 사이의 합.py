def solution(a, b):
    cnt = 0
    if a > b:
        a, b = b, a
    for n in range(a, b+1):
        cnt += n
    return cnt