def solution(s):
    words = list(map(str, s.split(" ")))
    capitalized_list = []
    
    for w in range(len(words)):
        capitalized_list.append(words[w].capitalize())

    answer = ""
    for capword in capitalized_list:
        chunk = capword + ' '
        answer += chunk
    # return " ".join(capitalized_list) join 쓰면 되는구나,,,, 
    # 가장 마지막 공백 슬라이싱 
    return answer[:-1] 
