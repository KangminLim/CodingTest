N, T = map(int,input().split())

dp = [0] * (T+1)
dp[0] = 0

lst = [list(map(int,input().split())) for _ in range(N)]

for k, s in lst:
    for i in range(T,k-1,-1): # 메모리, 절약을 위해 Top-bottom으로
        dp[i] = max(dp[i],dp[i-k]+s)
print(dp[-1])