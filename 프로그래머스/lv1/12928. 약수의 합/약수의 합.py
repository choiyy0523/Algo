def solution(n):
    cd = []
    for i in range(1, n+1):
        if n % i == 0:
            cd.append(i)

    return sum(cd)