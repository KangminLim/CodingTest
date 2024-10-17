N, K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]

dp = [0] * (K+1)
dp[0] = 0

for w,v in lst:
    for i in range(K,w-1,-1):
        dp[i] = max(dp[i],dp[i-w]+v)
print(dp[-1])