def jump(n):
    jump_num = []
    for i in range(1, n+1):
        if i == 1:
            jump_num.append(1)
        if i == 2:
            jump_num.append(2)
        if i > 2:
            jump_num.append(jump_num[i-2] + jump_num[i-3])
    return jump_num[n-1]

def solution(n):
    return jump(n) % 1234567