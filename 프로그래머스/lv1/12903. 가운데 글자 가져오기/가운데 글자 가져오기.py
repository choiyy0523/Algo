def solution(s):
    word = list(s)
    if len(word) % 2 == 0:
        answer = word[(len(word)//2)-1] + word[len(word)//2]
    else: 
        answer = word[len(word)//2]
        
    return answer