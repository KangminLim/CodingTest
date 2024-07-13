# 동전 2
N, K = map(int,input().split())
coins = set()
for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.add(coin)


dp = [100001] * (K+1)

dp[0] = 0

for coin in coins:
    for i in range(coin,K+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[-1] if dp[-1] != 100001 else -1)