coins = []
N, K = map(int,input().split())
for i in range(N):
    coins.append(int(input()))

# i원이 되는 경우의 수
dp = [0] * (K+1)
dp[0] = 1

# 코인의 종류를 바꿔가면서 진행
# 기존 코인으로 만든 것과 다른 코인으로 만들 수 있는 경우의 수룰 합치기
for coin in coins:
    for i in range(1,K+1):
        # i-coin : coin으로 i원 만드는 경우의 수 구해서 dp에 누적
        if i-coin >=0:
            dp[i] += dp[i-coin]

print(dp[K])