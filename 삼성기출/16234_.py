from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

ans = 0
q = deque()
while ans <= 2000:
    # [1] 전체를 순회하면서, 미방문 => 연합처리
    v = [[0] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] ==0:

                q.append((i, j))  # 큐에 초기데이터 삽입
                v[i][j] = 1  # 방문표시
                alst = [(i, j)]  # 엽한에 추가
                sm = arr[i][j]  # 합계

                while q:
                    ci, cj = q.popleft()
                    # 네방향, 범위내, 미주복, * 조건맞으면(L<=연구차이<=R)
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                            q.append((ni, nj))
                            v[ni][nj] = 1
                            alst.append((ni, nj))
                            sm += arr[ni][nj]
                if len(alst) > 1:
                    for ti, tj in alst:
                        arr[ti][tj] = sm // len(alst)
                    flag=1
    if flag==0:                           # 이동이 없었으면
        break
    ans += 1
print(ans)