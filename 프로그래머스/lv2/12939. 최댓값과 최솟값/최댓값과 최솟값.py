def solution(s):
    numbers = list(map(int,s.split(" ")))
    max_num = numbers[0]
    min_num = numbers[0]
    for n in range(len(numbers)) :
        if max_num <= numbers[n]:
            max_num = numbers[n]
    for n in range(len(numbers)) :
        if min_num >= numbers[n]:
            min_num = numbers[n]
    answer = str(min_num) + ' ' + str(max_num)

    return answer

# 일단 들어오는 문자열을 공백 기준으로 잘라서 리스트에 넣고, max min 으로 출력

