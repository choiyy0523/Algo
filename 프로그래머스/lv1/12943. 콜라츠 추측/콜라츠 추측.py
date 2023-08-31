def solution(num):
    cnt = 0
    
    while True :
        if num == 1:
            break
        if cnt > 500:
            break
        if num % 2 == 0:
            num = num // 2
            cnt += 1
        else:
            num = num*3 + 1
            cnt += 1
            
    if cnt >= 500:
        answer = -1
    else: 
        answer = cnt
    return answer