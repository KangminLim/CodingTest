# 파도반 수열
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    dp = [0] * 100
    dp[0] = dp[1] = dp[2] = 1
    N = int(input())

    for i in range(3,N):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[N-1])