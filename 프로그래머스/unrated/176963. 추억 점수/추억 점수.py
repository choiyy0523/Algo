def solution(name, yearning, photo):
    score = []
    for p in photo:
        tot = 0
        for ppl in p:
            for n in range(len(name)):
                if ppl == name[n]:
                    tot += yearning[n]
        score.append(tot)
    return score