def solution(progresses, speeds):
    answer = []
    # progresses에 작업이 남아있는 동안 계속 반복
    while len(progresses) != 0:
        # 배포한 기능 수
        cnt = 0
        # 만약 progresses에 작업이 남아있고, 가장 첫번째 작업의 진도가 100이라면
        while len(progresses) != 0 and progresses[0] >= 100:
            # 기능 배포 
            cnt += 1
            # 첫번째 작업 제거
            progresses.pop(0)
            speeds.pop(0)
        
        # 작업 진행
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        # 만약 기능이 배포되었다면 그날 배포된 기능 수를 answer에 추가
        if cnt != 0 :
            answer.append(cnt)
    
    return answer