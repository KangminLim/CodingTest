def solution(m, n, puddles):
    dp =[[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0: continue
            if [j+1,i+1] not in puddles:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]%1000000007