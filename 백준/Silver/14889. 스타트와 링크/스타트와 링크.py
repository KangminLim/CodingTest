def dfs(n,alst,blst):
    global ans
    if n==N:
        if len(alst) == len(blst):
            asm = bsm = 0
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]
            ans = min(ans,abs(asm-bsm))
        return
    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = N//2
ans =100*M*M

dfs(0,[],[])
print(ans)