# 스타트와 링크

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def cal(alst,blst):
    asm = bsm = 0
    for i in range(M):
        for j in range(M):
            asm += arr[alst[i]][alst[j]]
            bsm += arr[blst[i]][blst[j]]
    return abs(asm-bsm)

def dfs(n, alst, blst):
    global ans
    if n == N :
        if len(alst) == len(blst):
            ans = min(ans,cal(alst,blst))
        return
    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])

M = N//2
ans = 100 * M * M
dfs(0,[],[])
print(ans)사