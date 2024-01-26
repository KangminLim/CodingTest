# 유기농 배추
from collections import deque
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            nx = now[0] + dx[k]
            ny = now[1] + dy[k]
            if 0<=nx<M and 0<=ny<N and mp[nx][ny]==1 and not visited[nx][ny]:
                mp[nx][ny] = 2
                queue.append((nx,ny))


for tc in range(T):
    M, N, K = map(int, input().split())
    mp = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        mp[x][y] = 1

    for a in range(M):
        for b in range(N):
            if mp[a][b] == 1 and not visited[a][b]:
                BFS(a,b)
                cnt+=1
    print(cnt)