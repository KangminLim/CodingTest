# 링크와 스타트
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

def dfs(n,alst,blst):
    global ans
    if n == N:
        asm = bsm = 0
        an = len(alst)
        bn = len(blst)
        for i in range(an):
            for j in range(an):
                asm += lst[alst[i]][alst[j]]

        for i in range(bn):
            for j in range(bn):
                bsm += lst[blst[i]][blst[j]]
        ans = min(ans,abs(asm-bsm))
        return

    # A팀 선택
    dfs(n+1,alst+[n],blst)
    # B팀 선택
    dfs(n+1,alst,blst+[n])

ans = 100*N*N
dfs(0,[],[])

print(ans)