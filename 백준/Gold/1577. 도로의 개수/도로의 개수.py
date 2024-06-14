N, M = map(int,input().split())
K = int(input())

# 2차원 리스트에 튜플로 공사장을 저장
construction = [[[] for _ in range(M+1)] for _ in range(N+1)]
for _ in range(K):
    a,b,c,d = map(int,input().split())
    construction[a][b].append((c,d))
    construction[c][d].append((a,b))

# 2차원 dp 배열 만들기
dp = [[0] * (M+1) for _ in range(N+1)]
# dp 초깃값 설정
dp[0][0] = 1

for i in range(N+1):
    for j in range(M+1):
        # 현재 위치에서 위쪽이 범위를 벗어나지 않고 공사장에 사람이 있는지 확인
        if i-1 >= 0 and (i-1,j) not in construction[i][j]:
            dp[i][j] += dp[i-1][j]
        # 현재 위치에서 왼쪽이 범위를 벗어나지 않고 공사장에 사람이 있는지 확인
        if j-1 >= 0 and (i,j-1) not in construction[i][j]:
            dp[i][j] += dp[i][j-1]
print(dp[-1][-1])


