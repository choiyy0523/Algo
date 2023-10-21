def solution(array, n):
    cnt = 0
    
    for number in array:
        if number == n:
            cnt += 1
            
    return cnt