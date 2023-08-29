def solution(s):
    cntP = 0
    cntY = 0
    
    for c in list(s):
        if c == 'P' or c == 'p':
            cntP += 1
        if c == 'Y' or c == 'y':
            cntY += 1
        
    if cntP == cntY:
        return True
    else:
        return False

## 아예 전부 lower로 돌리고 count() 써도 됨