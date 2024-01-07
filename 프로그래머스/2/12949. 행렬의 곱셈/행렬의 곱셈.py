def solution(arr1, arr2):
    M = len(arr1[0])   # arr1 가로  2
    N = len(arr1)      # arr1 세로  3
    J = len(arr2[0])   # arr2 가로  2
    K = len(arr2)      # arr2 세로  2
    
    result = [[0] * J for _ in range(N)]  # 2, 3 [[0, 0], [0, 0], [0, 0]]
    
    for n in range(N):   
        for j in range(J):  
            for m in range(M):
                result[n][j] += arr1[n][m] * arr2[m][j] 

    return result