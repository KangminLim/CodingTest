# 치즈
N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[False] * M for _ in range(N)]
    v[si][sj] = True
    total = 0
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<M and not v[ni][nj]:
                if arr[ni][nj] == 0:
                    q.append((ni,nj))
                    v[ni][nj] = True
                elif arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    v[ni][nj] = True
                    total += 1
    return total

alst = []
ans = 0
while True:
    alst.append(bfs(0,0))
    ans += 1
    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt == 0:
        break

print(ans)
print(alst[-1])