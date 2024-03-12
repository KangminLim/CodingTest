from collections import deque
def bfs(i,j):
    dx , dy = [0,0,1,-1], [1,-1,0,0]
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]

def solution(maps):
    global graph
    global n,m
    n = len(maps)
    m = len(maps[0])
    graph = maps
    answer = bfs(0,0)
    if answer <= 1:
        return -1
    return answer

