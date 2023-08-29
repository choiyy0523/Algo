def solution(numbers):
    answer = []
    for n in range(0, 10):
        if n not in numbers:
            answer.append(n)
    return sum(answer)