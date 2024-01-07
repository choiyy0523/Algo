def solution(answers):
    # 패턴 분석
    # 1번 수포자 : 12345 반복
    # 2번 수포자 : 21 23 24 25 반복
    # 3번 수포자 : 33 11 22 44 55 반복

    scores = [0, 0, 0]
    ans = len(answers)

    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in list(range(ans)):
        if answers[i] == stu1[i % 5]:
            scores[0] += 1
        if answers[i] == stu2[i % 8]:
            scores[1] += 1
        if answers[i] == stu3[i % 10]:
            scores[2] += 1
    
    # 가장 많이 맞춘 사람들만 return 하면 된다
    max_score = max(scores)
    rtn = []
    
    # print(list(enumerate(scores))) # [(0, 5), (1, 0), (2, 0)]
    
    # 가장 많이 맞춘 사람이 여러 명일 경우 처음부터 순회하면서 append하면 자동으로 오름차순으로 정렬된다 
    for i, score in enumerate(scores):
        if score == max_score:
            rtn.append(i+1)

    return rtn