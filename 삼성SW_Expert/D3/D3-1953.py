def bfs(N,M):
    # 좌, 상, 우, 하
    way = [(0,-1),(-1,0),(0,1),(1,0)]
    pipe = [[],[0,1,2,3],[1,3],[0,2],[1,2],[3,2],[3,0],[1,0]]
    while q:
        x, y =q.pop(0)
        sub = pipe[fig[x][y]]
        if sub ==[]:
            continue
        for i in sub:
            di, dj = way[i]
            nx, ny = x + di , y+dj
            if 0 <= nx < N and 0<=ny<M and visited[nx][ny] == 0 and fig[nx][ny] != 0:
                next = pipe[fig[nx][ny]]
                for j in next:
                    mx, my = = nx+way[j][0], ny+way[j][1]
                    if mx == x and my ==y:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y]+1

T = int(input())
for tc in range(T):
    # N,M : 지도의 세로, 가로
    # R,C : 맨홀 뚜껑의 세로, 가로(출발점)
    # L : 탈출 후 소요된 시간
    N,M,R,C,L = map(int,input().split())
    fig =[list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    q =[(R,C)]
    bfs(N,M)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1