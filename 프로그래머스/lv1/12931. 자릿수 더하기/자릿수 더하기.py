def solution(n):
    answer_list = list(str(n))
    answer = 0
    for i in answer_list:
        answer += int(i)
    return answer