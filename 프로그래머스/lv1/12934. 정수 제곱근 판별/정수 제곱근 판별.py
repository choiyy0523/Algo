def solution(n):
    x = int(n**(0.5))
    if x**2 == n:
        return (x+1)**2
    else:
        return -1
        