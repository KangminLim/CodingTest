# def solution(n):
#     dp = [0] * (n+1)
#     dp[0] = 1
#     dp[1] = 2
#     for i in range(2,n):
#         dp[i] = dp[i-1]+dp[i-2]
#     print(dp)
#     return dp[n-1]%1234567
def solution(n):
    if n == 1:
        return 1
    
    a = 1
    b = 2
    for i in range(2,n):
        a, b = b, a+b
    return b%1234567