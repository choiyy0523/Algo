def solution(n, lost, reserve):
    # 지금 아래에서 l-1 in reserve를 먼저 체크하고 있기 때문에, sort 안해주면 번호가 적은 사람이 체육복을 못 빌리는 경우가 생김
    # ex. lost = [4, 2], reserve = [5, 3] -> 4가 3을 먼저 가져가버리기 때문에 2, 4 모두 빌릴 수 있음에도 불가능해짐
    lost.sort()
    reserve.sort()
    
    check = [0] * n
    # 0. 일단 수업 들을 수 있는 사람들 체크
    for i in range(n):
        if i+1 not in lost:
            check[i] = 1
        
    # 1. 체육복을 가져온 학생이 도난 당했는지 확인
    # -> 만약 도난당했을 경우, lost와 reserve에서 제거 필요
    for i in range(n):
        if (i+1 in lost) and (i+1 in reserve):
            lost.remove(i+1)
            reserve.remove(i+1)
            check[i] = 1
            
    # 2. lost를 순회하며 앞뒤로 체육복 빌려줄 수 있는 사람이 있는지 체크
    for l in lost:
        if l-1 in reserve:
            check[l-1] = 1
            reserve.remove(l-1)
                
        elif l+1 in reserve:
            check[l-1] = 1 
            reserve.remove(l+1)
                                    
    return check.count(1)