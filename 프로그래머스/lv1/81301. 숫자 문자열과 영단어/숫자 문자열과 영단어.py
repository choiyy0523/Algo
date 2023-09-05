def solution(s):
    # 문자열이 연달아 나올 수도 있으므로(zeroonetwo 등) 다음 숫자가 나올 때 까지 받아서 join 하고 pop하는건 비효율적
    num_dicts = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    for num in num_dicts.keys():
        if num in s:
            s = s.replace(num, num_dicts[num]) # replace는 다시 받아줘야 변경적용됨 
    return int(s)
