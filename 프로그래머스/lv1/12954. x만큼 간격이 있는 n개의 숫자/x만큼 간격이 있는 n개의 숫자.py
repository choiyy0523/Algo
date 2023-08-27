def solution(x, n):
    answer = []
    cnt = 0
    plus = x
    while cnt < n:
        answer.append(x)
        x += plus
        cnt += 1
    return answer