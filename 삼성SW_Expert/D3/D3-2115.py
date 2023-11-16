T=int(input())

def dfs(n,cnt,sm,ci,cj):
    global mx
    if cnt>C: # 합친 꿀의 양이 C보다 큰 경우
        return
    if n==M:
        mx =max(mx,sm)
        return
    dfs(n+1,cnt+arr[ci][cj+n],sm+arr[ci][cj+n]**2,ci,cj)
    dfs(n+1,cnt,sm,ci,cj)

for test_case in range(1,T+1):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = mx = 0
    mem=[[0]*N for _ in range(N)]
    # [0] 각 위치의 가능한 최대값을 한 번 저장
    # 동일한 위치에서 dfs를 호출해서 중복연산 방지
    for i in range(N):
        for j in range(N - M + 1):
            mx =0
            dfs(0,0,0,i,j)
            mem[i][j]=mx
    # [1] 가능한 모든 시작위치(일꾼 1,2)
    for i1 in range(N):
        for j1 in range(N - M + 1):
            for i2 in range(i1, N):
                sj = j1 + M if i1 == i2 else 0
                for j2 in range(sj, N - M + 1):
                    ans = max(ans,mem[i1][j1]+mem[i2][j2])

    # # [1] 가능한 모든 시작위치(일꾼 1,2)
    # for i1 in range(N):
    #     for j1 in range(N-M+1):
    #         mx = 0
    #         dfs(0,0,0,i1,j1)
    #         sm1 = mx    # 일꾼 1, 본 위치 최대값
    #         for i2 in range(i1,N):
    #             sj = j1+M if i1==i2 else 0
    #             for j2 in range(sj,N-M+1):
    #                 mx = 0
    #                 dfs(0,0,0,i2,j2)
    #                 ans = max(ans,sm1+mx)
    print()