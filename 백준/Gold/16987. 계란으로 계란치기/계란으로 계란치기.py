# 계란으로 계란 치기 (뺵트래킹)
def dfs(n,cnt):
    global ans

    if n == N:
        ans = max(cnt,ans)
        return

    if lst[n][0] <= 0: # 현재 계란이 깨진 경우 => 다음 계란
        dfs(n+1,cnt)

    else: # 현재 계란 안깨진 상태
        flag = False

        for j in range(N): # 하나씩 부딪쳐보기
            if n == j or lst[j][0] <= 0: continue
            flag = True
            lst[n][0] -= lst[j][1]
            lst[j][0] -= lst[n][1]
            dfs(n+1, cnt + int(lst[n][0]<=0) + int(lst[j][0]<=0))
            lst[n][0] += lst[j][1]
            lst[j][0] += lst[n][1]
        if not flag:
            dfs(n+1,cnt)

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

ans = 0
dfs(0,0)
print(ans)