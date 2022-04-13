

N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp =[[0 for _ in range(N)] for _ in range(N)] 


for i in range(1, N): # 부분문제 크기
    
    for j in range(0, N-i):
        if i == 1: #차이가 1밖에 나지 않는 칸
            dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue
        
        dp[j][j+i] = 2**32 # 최댓값을 미리 넣어줌
        for k in range(j, j+i):
            temp = dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1]
            if dp[j][j+i] > temp : # 원래 들어있던 값보다 곱셈 횟수가 적으면 교체
                dp[j][j+i] = temp 
        
    
print(dp[0][N-1])

