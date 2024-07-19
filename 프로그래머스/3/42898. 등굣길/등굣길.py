def solution(m, n, puddles):
    answer = 0
    # dp 초기화
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i,j) == (0,0): continue
            if [j+1,i+1] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]%1000000007