def solution(s):
    gh = list(map(str,s))
    stack = []
    if len(gh) % 2 == 1:  # 일단 전체가 홀수면 무조건 False
        answer = False
    elif gh[0] == ')':    # 시작이 닫는 괄호면 무조건 False
        answer = False 
    elif gh[-1] == '(' :  # 끝이 여는 괄호면 무조건 False
        answer = False
    else :    
        for g in gh:
            if g == '(':
                stack.append(g)
            else:
                if len(stack) != 0:
                    stack.pop()        
        if len(stack) == 0:
            answer = True
        else : 
            answer = False
    return answer