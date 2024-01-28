# 유기농 배추 (bfs를 통한 풀이)
from collections import deque
T = int(input())
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[j][i] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            nx = now[0] + dx[k]
            ny = now[1] + dy[k]
            if 0<=nx<M and 0<=ny<N and mp[ny][nx]==1 and not visited[ny][nx]:
                mp[ny][nx] = 2
                queue.append((nx,ny))


for tc in range(T):
    M, N, K = map(int, input().split())
    mp = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        mp[y][x] = 1

    for i in range(M):
        for j in range(N):
            if mp[j][i] == 1 and not visited[j][i]:
                BFS(i,j)
                cnt+=1
    print(cnt)