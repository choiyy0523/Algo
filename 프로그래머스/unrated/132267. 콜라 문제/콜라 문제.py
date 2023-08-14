def solution(a, b, n):
    cnt = 0
    total_coke = n
    
    while total_coke >= a:
        trade_coke = (total_coke // a) * b
        cnt += trade_coke
        total_coke = trade_coke + total_coke % a 

    return cnt