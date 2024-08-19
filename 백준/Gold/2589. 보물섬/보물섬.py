# 보물섬
R, C = map(int,input().split())
arr = [list(map(str,input())) for _ in range(R)]

from collections import deque
ans = 0

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v = [[0] * C for _ in range(R)]
    v[si][sj] = 1
    while q:
        ci,cj = q.popleft()

        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<R and 0<=nj<C and not v[ni][nj] and arr[ni][nj] =='L':
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1

    return max(map(max,v))


for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            tmp = bfs(i,j)
            ans = max(tmp,ans)
print(ans-1)

