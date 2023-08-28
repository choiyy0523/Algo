def solution(n):
    test = list(str(n))
    test.sort(reverse=True)
    return int(''.join(test))