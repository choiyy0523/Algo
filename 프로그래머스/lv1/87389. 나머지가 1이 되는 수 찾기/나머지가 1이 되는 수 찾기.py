def solution(n):
    answer_list = []
    for i in range(1, n):
        if n % i == 1:
            answer_list.append(i)
            
    return min(answer_list)