def solution(numbers):
    numbers.sort() # 1 1 2 3 4
    n = len(numbers) 
    answer = []
    for i in range(n):  
        for j in (range(i+1, n)): 
            answer.append(numbers[i]+numbers[j])
    tmp = list(set(answer))
    tmp.sort()
    return tmp