# import sys
# input = sys.stdin.readline
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [[-1] * M for _ in range(N)]

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 0
    while q:
        ci,cj = q.popleft()
        # if arr[ci][cj] == 2:
        #     nlst[si][sj] = v[ci][cj]
        #     return
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == -1:
                if arr[ni][nj] == 1:
                    v[ni][nj] = v[ci][cj] + 1
                    q.append((ni,nj))


for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            si,sj = i,j
            break
bfs(si,sj)

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            v[i][j] = 0

for row in v:
    print(*row)
