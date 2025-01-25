# LIS
N = int(input())
lst = list(map(int,input().split()))
lst.reverse()

dp = [1] * N

# LIS 가장 긴 증가하는 부분 수열 수행
for i in range(1,N):
    for j in range(0,i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))