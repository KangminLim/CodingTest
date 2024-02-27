# 유기농 배추
from collections import deque
T = int(input())


def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and mp[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((nx, ny))

for tc in range(T):
    M, N, K = map(int,input().split())
    mp = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0
    for _ in range(K):
        x,y = map(int,input().split())
        mp[y][x] = 1

    for a in range(M):
        for b in range(N):
            if mp[b][a] == 1 and not visited[b][a]:
                bfs(a,b)
                cnt += 1

    print(cnt)
