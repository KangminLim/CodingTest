N, M = map(int,input().split())
K = int(input())
construction = [[[] for _ in range(M+1)] for _ in range(N+1)]

for _ in range(K):
    a,b,c,d = map(int,input().split())
    construction[a][b].append((c,d))
    construction[c][d].append((a,b))

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N+1):
    for j in range(M+1):
        if i-1 >= 0 and (i-1,j) not in construction[i][j]:
            dp[i][j] += dp[i-1][j]
        if j-1 >= 0 and (i,j-1) not in construction[i][j]:
            dp[i][j] += dp[i][j-1]

print(dp[-1][-1])