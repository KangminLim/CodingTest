# def cal(alst,blst):
#     asm=bsm=0
#     for i in range(M):
#         for j in range(M):
#             asm += arr[alst[i]][alst[j]]
#             bsm += arr[blst[i]][blst[j]]
#     return abs(asm-bsm)

def dfs(n,alst,blst):
    if ans==0:
        return

    # 한팀이 이미 M명 초과인 경우
    if len(alst)>M or len(blst)>M:
        return

    if n ==N:
        if len(alst)==len(blst):
            ans = min(ans,abs(asm-bsm))
        return
    dfs(n+1,alst+[n],blst) # A팀
    dfs(n+1,alst,blst+[n]) # B팀

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

M = N//2

ans = 100*M*M
dfs(0,[],[])
print(ans)