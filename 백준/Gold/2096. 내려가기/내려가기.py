import sys

input = sys.stdin.readline

# 배열 크기 입력 받기
N = int(input())

a,b,c = map(int,input().split())

dp = [[] for _ in range(2)]

dp[0] = [a,b,c]
dp[1] = [a,b,c]

for _ in range(N-1):
    a,b,c = map(int,input().split())

    # 최대
    dp[0][0], dp[0][1], dp[0][2] = a+max(dp[0][0],dp[0][1]),b+max(dp[0][0], dp[0][1], dp[0][2]),c+max(dp[0][1], dp[0][2])
    # 최소
    dp[1][0], dp[1][1], dp[1][2] = a+min(dp[1][0],dp[1][1]),b+min(dp[1][0], dp[1][1], dp[1][2]),c+min(dp[1][1], dp[1][2])


print(max(dp[0]),min(dp[1]),end=' ')