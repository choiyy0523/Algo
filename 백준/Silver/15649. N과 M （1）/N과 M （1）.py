import sys

# sys.stdin = open('input.txt')

# <SOLUTION 1>
# N, M = map(int, sys.stdin.readline().split())
# answer = []
#
# def backtrack():
#     # 원하는 길이의 수열이 만들어 졌다면 출력하고 return
#     if len(answer) == M:
#         print(' '.join(map(str,answer)))  # join은 str에만 쓸 수 있음!
#         return
#
#     for i in range(1, N+1):
#         # 일단 answer에 없으면 answer에 추가하고 재귀
#         if i not in answer:
#             answer.append(i)
#             backtrack()
#             # 끝값 바꿔줌
#             answer.pop()
#
# backtrack()

# <SOLUTION 2>
# 반복될 재귀함수
# s의 길이가 M과 같아지면 원하는 형태로 값 출력 후 return
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        # 만약 해당 위치를 방문했다면 visited[i] == True 라면 아래 부분을 건너 뛰고 i += 1을 실행
        if visited[i]:
            continue

        # 방문 안한 곳이라면 일단 방문 처리
        visited[i] = True
        s.append(i)
        # 재귀
        dfs()

        # 마지막 부분 삭제
        s.pop()

        # 방문 처리 원복
        visited[i] = False

N, M = map(int, sys.stdin.readline().split())
s = []
visited = [False] * (N+1)
dfs()