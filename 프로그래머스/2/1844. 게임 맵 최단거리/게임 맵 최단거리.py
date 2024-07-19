from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    def bfs(ci,cj):
        q = deque()
        q.append((ci,cj))
        v = [[0] * M for _ in range(N)]
        v[ci][cj] = 1
        
        while q:
            ci,cj = q.popleft()
            if (ci,cj) == (N-1,M-1):
                return v[N-1][M-1]
            
            for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                if 0<=ni<N and 0<=nj<M and not v[ni][nj] and maps[ni][nj]:
                    q.append((ni,nj))
                    v[ni][nj] = v[ci][cj] + 1
                    
        return -1 
    
    answer = bfs(0,0)
    
    return answer