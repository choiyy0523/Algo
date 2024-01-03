def solution(n, lost, reserve):
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