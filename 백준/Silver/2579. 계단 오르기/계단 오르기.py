N = int(input())
stairs = [0] * 301
for i in range(1,N+1):
    stairs[i] = int(input())
dp = [0] * 301

dp[1] = stairs[1]
dp[2] = dp[1] + stairs[2]

for i in range(3,N+1):
    dp[i] = max(dp[i-2],dp[i-3]+stairs[i-1]) + stairs[i]

print(dp[N])