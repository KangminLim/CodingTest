from collections import deque
def solution(board):
    answer = 0
    N = len(board)
    di,dj = [0,1,0,-1],[1,0,-1,0]
    def bfs(si,sj,sd):
        q = deque()
        q.append((si,sj,sd,0))
        v = [[int(1e9)] * len(board[0]) for _ in range(len(board))]
        v[si][sj] = 0
        while q:
            ci,cj,cd,cost = q.popleft()
            for i in range(4): 
                ni,nj = ci+di[(cd+i)%4],cj+dj[(cd+i)%4]
                if 0<=ni<N and 0<=nj<N and board[ni][nj] ==0:
                    if i == 0:
                        ncost = cost + 100
                    else:
                        ncost = cost + 600
                    if ncost < v[ni][nj]:
                        v[ni][nj] = ncost
                        q.append((ni,nj,(cd+i)%4,ncost))
        return v[-1][-1]
    
    answer = min(bfs(0,0,0),bfs(0,0,1))
    
    return answer