# 인구 이동
from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj)) # 큐에 초기 데이터 삽입
    v[si][sj] = 1 # 방문 표시
    alst = [(si,sj)] # 연합에 추가
    sm = arr[si][sj] # 합계

    while q:
        ci,cj = q.popleft()
        # 네 방향, 범위 내, 미중복, *조건 맞으면(L <= 인구차이 <= R)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and L <= abs(arr[ci][cj]-arr[ni][nj]) <= R:
                q.append((ni,nj))
                v[ni][nj] = 1
                alst.append((ni,nj))
                sm += arr[ni][nj]
    if len(alst) > 1: # 연합인 경우 처리(평균값 각각 저장)
        for ti,tj in alst:
            arr[ti][tj] = sm // len(alst)
        return 1 # 연합이 있는 경우 1 리턴
    return 0 # 없으면 0 리턴

N, L, R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
while ans <= 2000:
    # [1] 전체를 순회하면서, 미방문 => 연결된 연합 처리
    v = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:   # 미방문
                flag = max(flag,bfs(i,j))       # bfs => 연합이 있었으면 1
    if flag == 0:
        break

    ans += 1

print(ans)