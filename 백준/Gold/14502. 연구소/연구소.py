N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
virus = [] 
change_wall = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i,j))
        elif arr[i][j] == 0:
            change_wall.append((i,j))
    
from itertools import combinations
from collections import deque

ans = 0

def bfs(si,sj,v,arr):
    q = deque()
    q.append((si,sj))
    v[si][sj] = True

    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = True
                arr[ni][nj] = 2


for comb in combinations(change_wall,3):
    narr = [x[:] for x in arr]
    for ci,cj in comb:
        narr[ci][cj] = 1

    tmp = 0
    # print('')
    v = [[False] * M for _ in range(N)]
    for ci,cj in virus:
        bfs(ci,cj,v,narr)
    # print('')
    for lst in narr:
        tmp += lst.count(0)
    # print('')
    if tmp > ans:
        ans = tmp

    for ci, cj in comb:
        narr[ci][cj] = 0

print(ans)