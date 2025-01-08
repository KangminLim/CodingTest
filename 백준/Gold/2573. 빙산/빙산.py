import sys
input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True
    groups[-1].add((si,sj))
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] > 0 and not v[ni][nj]:
                q.append((ni,nj))
                v[ni][nj] = True
                groups[-1].add((ni,nj))
ans = 0
while True:
    cnt = N * M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt == 0:
        ans = 0
        break
    v = [[False] * M for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not v[i][j]:
                groups.append(set())
                bfs(i, j)
    # print('')
    if len(groups) > 1:
        break

    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                for ni, nj in ((i-1,j),(i,j+1),(i+1,j),(i,j-1)):
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                        narr[i][j] = max(0,narr[i][j] - 1)
                        flag = True
    # print('')
    arr = narr
    ans += 1

print(ans)