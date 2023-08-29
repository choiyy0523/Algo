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
