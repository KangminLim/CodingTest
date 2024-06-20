N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

air = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            air.append((i,j))

di,dj = [-1,0,1,0], [0,1,0,-1]
opp1 = {0:0,1:3,2:2,3:1}
opp2 = {0:2,1:1,2:0,3:3}
opp3 = {0:1,1:0,2:3,3:2}
opp4 = {0:3,1:2,2:1,3:0}


from collections import deque
def bfs(si,sj):

    for k in range(4):
        dr = k
        q = deque()
        q.append((si, sj))
        v[si][sj] += 1
        while q:
            ci, cj = q.popleft()
            ni,nj = ci+di[dr], cj+dj[dr]
            if 0<=ni<N and 0<=nj<M and v[ni][nj] < 4 :
                q.append((ni,nj))
                v[ni][nj] += 1
                if arr[ni][nj] == 1:
                    dr = opp1[dr]
                elif arr[ni][nj] == 2:
                    dr = opp2[dr]
                elif arr[ni][nj] == 3:
                    dr = opp3[dr]
                elif arr[ni][nj] == 4:
                    dr = opp4[dr]
                elif arr[ni][nj] == 9:
                    break

v = [[0] * M for _ in range(N)]
for ai,aj in air:
    bfs(ai,aj)
ans = N*M
for t in v:
    ans -= t.count(0)
print(ans)