def solution(k, tangerine):
    tangerine_dict = {}
    for t in list(set(tangerine)):  # 귤 종류를 key로 설정
        tangerine_dict[t] = 0       # 처음 귤 갯수 전부 0개로 설정
    for t in tangerine:             # 전체 tangerine을 순회하면서
        tangerine_dict[t] += 1      # key 값이 t인 것의 value에 1을 더함
        
    tangerine_dict_sorted = sorted(tangerine_dict.items(), key=lambda x: x[1], reverse=True)
    
    answer = 0
    for t in tangerine_dict_sorted:
        if k <= 0 :
            break
            # 음수가 되면 마지막 종류의 귤을 전부 쓰지 않고 일부만 사용했다는 뜻 
        else:
            k -= t[1]
            answer += 1
    return answer
