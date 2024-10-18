import sys
input = sys.stdin.readline
N = int(input())

a,b,c = map(int,input().split())

dp = [[] for _ in range(2)]

dp[0] = [a,b,c] # 최소
dp[1] = [a,b,c] # 최대

for _ in range(N-1):
    a,b,c = map(int,input().split())
    # dp[0][0],dp[0][1],dp[0][2] = min(dp[0][0]+a,dp[0][0]+b), min(dp[0][0]+a,dp[0][1]+b,dp[0][2]+c), min(dp[0][2]+b,dp[0][2]+c)
    # dp[1][0],dp[1][1],dp[1][2] = max(dp[1][0]+a,dp[1][0]+b), max(dp[1][0]+a,dp[1][1]+b,dp[1][1]+c), max(dp[1][2]+b,dp[1][2]+c)
    dp[0][0], dp[0][1], dp[0][2] = a+min(dp[0][0],dp[0][1]), b+min(dp[0][0],dp[0][1],dp[0][2]), c+min(dp[0][1],dp[0][2])
    dp[1][0], dp[1][1], dp[1][2] = a+max(dp[1][0],dp[1][1]), b+max(dp[1][0],dp[1][1],dp[1][2]), c+max(dp[1][1],dp[1][2])
print(max(dp[1]),min(dp[0]))