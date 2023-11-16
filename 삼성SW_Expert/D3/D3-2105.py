


di = [1,1,-1,-1,1]
dj = [-1,1,1,-1,-1]
def dfs(n,ci,cj,v):
    global ans
    # 가지치기: 절반을 돌았는데 *2 해도 정답 갱신 불가능
    if n==2 and ans>=len(v*2):
        return
    if n>3:
        return
    if n==3 and (si,sj) ==(ci,cj):
        ans = max(ans,len(v))
        return
    for k in range(n,n+2):
        ni,nj = ci+di[k], cj+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(k,ni,nj,v)
            v.pop()

T=int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = -1
    for si in range(N-2):
        for sj in range(1,N-1):
            dfs(0,si,sj,[])
    print(f'#{test_case} {ans}')