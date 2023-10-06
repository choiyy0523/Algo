def solution(num_list):
    new_list = []
    for num in range(len(num_list)-1, -1, -1):
        new_list.append(num_list[num])
    return new_list