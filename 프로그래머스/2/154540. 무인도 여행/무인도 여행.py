from collections import deque
def bfs(maps,si,sj,N,M,v):  
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    area = int(maps[si][sj])
    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(0,1),(1,0),(0,-1)):
            ni,nj = ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and maps[ni][nj] != 'X':
                q.append((ni,nj))
                v[ni][nj] = 1
                area += int(maps[ni][nj])
    return area
                
                
def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    v = [[False] * (M) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not v[i][j]:
                answer.append(bfs(maps,i,j,N,M,v))
    if answer:
       return sorted(answer)
    else: return [-1]
               
