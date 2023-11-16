p = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
opp = [1,0,3,2]
di, dj = [-1,1,0,0] ,[0,0,-1,1]
def bfs(si,sj):
    q = []
    v = [[0]* M for _ in range(N)]
    ans = 0

    # q에 삽입할 때
    q.append((si,sj))
    v[si][sj] = 1
    ans += 1

    while q:
        ci, cj = q.pop(0)
        if v[ci][cj] == L:
            return ans
        # 4방향, 범위내, 중복 x, 조건(현위치-이동할 위치 모두 파이프 있는 경우)에 맞으면 q 삽입
        for dr in range(4):
            ni,nj = ci+di[dr], cj+dj[dr]
            # 문제 조건
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and p[arr[ci][cj]][dr] == 1 and p[arr[ni][nj]][opp[dr]] == 1:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1
                ans += 1
    return ans # 가능한 위치보다 더 긴 시간을 준 경우 ..

T = int(input())
for test_case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = bfs(R,C)
    print(f'#{test_case} {ans}')