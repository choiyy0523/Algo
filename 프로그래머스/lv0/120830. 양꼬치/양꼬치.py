def solution(n, k):
    service = n//10
    tot = 12000*n + 2000*(k-service)
    return tot