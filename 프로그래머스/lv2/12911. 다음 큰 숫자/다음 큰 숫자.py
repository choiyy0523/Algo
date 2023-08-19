# 2진수로 변환하는 함수
def binary(num):
    bin_nums = []
    while num > 1:
        num, div = num // 2, num % 2
        bin_nums.append(str(div))
    if num == 1:
        bin_nums.append(str(1))

    answer = ''
    for i in range(-1, -1 * (len(bin_nums) + 1), -1):
        answer += bin_nums[i]

    return answer

# 변환한 2진수 내 1의 갯수 카운트 함수 
def check_1(n):
    cnt = 0
    for c in n:
        if c == '1':
            cnt += 1
    return cnt

def solution(n):
    cnt1 = check_1(binary(n))
    while True:
        n += 1
        cnt2 = check_1(binary(n))
        if cnt2 == cnt1:
            break

    return n
