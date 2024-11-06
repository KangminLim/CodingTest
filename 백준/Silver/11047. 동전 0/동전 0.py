import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins = coins[::-1]
ans = 0
for coin in coins:
    if coin > K: continue
    if K == 0: break
    ans += K//coin
    K %= coin
print(ans)