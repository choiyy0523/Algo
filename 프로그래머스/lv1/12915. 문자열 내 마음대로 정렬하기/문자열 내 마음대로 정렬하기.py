def solution(strings, n):
    for i in range(len(strings)):
        for j in range(0, len(strings)-i-1):
            if strings[j][n] > strings[j+1][n]:
                strings[j], strings[j+1] = strings[j+1], strings[j]
            elif strings[j][n] == strings[j+1][n]:
                if strings[j] > strings[j+1]:
                    strings[j], strings[j+1] = strings[j+1], strings[j]
    return strings