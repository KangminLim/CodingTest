# dp[1] = 1 / dp[2] = (1,1), (2) / dp[3] (1,1,1) (2,1) (1,2) / dp[4] = 5 
def solution(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%1234567