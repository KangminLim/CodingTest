M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
slst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            slst.append((i,j))

from collections import deque

def bfs(lst):
    q = deque()
    v = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                v[i][j] = True

    for si,sj in lst:
        q.append((si,sj))
        v[si][sj] = True
    time = 0
    while q:
        ci,cj = q.popleft()

        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj] == 0:
                q.append((ni,nj))
                arr[ni][nj] = arr[ci][cj] + 1

bfs(slst)

result = 0
for row in arr:
    for j in row:
        if j==0:
            print(-1)
            exit()
    else:
        result = max(result,max(row))
print(result-1)

