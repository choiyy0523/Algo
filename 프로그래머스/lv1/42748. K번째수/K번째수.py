def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        new_array = sorted(array[start:end])
        # print(new_array)
        answer.append(new_array[command[2]-1])
    return answer