# 빽트래킹 -> 값이 커지면 힘듬
def dfs(n, sm):
    global ans
    # [1] 종료조건 : 가능한 n을 종료에 관련된 것으로 정의!
    if n>=N:
        ans = max(ans,sm)
        return
    # [2] 하부호출 : 화살표 개수만큼 호출
    if n+T[n] <= N : # 상담하는 경우(퇴사일전 완료 가능할 때만 상담)
        dfs(n+T[n],sm+P[n])
    # 상담하지 않는 경우(항상 가능)
    dfs(n+1,sm)


N = int(input())
T = [0] * N
P= [0] * N
for i in range(N):
    T[i], P[i] = map(int,input().split())

ans = 0
dfs(0,0)
print(ans)

# DP
dp = [0]*(N+1)
for n in range(N-1,-1,-1):
    if n+T[n] <=N:
        dp[n] = max(dp[n-1], dp[n+T[n]] + P[n])
    else:
        dp[n] =dp[n+1]

print(dp[0])