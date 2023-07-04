def fibo(n):
    fibo_num = [] 
    for i in range(n+1): 
        if i == 0:
            fibo_num.append(0)
        elif i == 1:
            fibo_num.append(1)
        elif i >= 2:
            fibo_num.append(fibo_num[i-1] + fibo_num[i-2])
            
    # print(fibo_num)
            
    return fibo_num[n]

def solution(n):
    answer = fibo(n) % 1234567
    return answer 