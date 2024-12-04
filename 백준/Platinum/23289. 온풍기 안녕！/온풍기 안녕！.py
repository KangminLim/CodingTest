di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]
R,C,K = map(int,input().split())
arr = [[0] * (C+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(R)] + [[0] * (C+2)]

# [0] 벽 만들기 : 이동 방향에 따라서 이동할 수 없는 경우 벽 룩업테이블 만들기
W = int(input())
wall = [[[0] * 5 for _ in range(C+2)] for _ in range(R+2)] # 벽 표시를 위해
for _ in range(W):
    i,j,t = map(int,input().split())
    if t==0: # 위로 갈 때, 위에서 현재 위치(아래) 올 때
        wall[i][j][3] = wall[i-1][j][4] = 1
    else: # 오른쪽으로 갈 때, 오른쪽에서 현재 위
        wall[i][j][1] = wall[i][j+1][2] = 1

# [0] 온풍기 위치 및 방향 저장, 온도 조절 위치 저장
mlst = [] # 온도 측정
hlst = [] # 온풍기(시작좌표, 방향)

for i in range(1,R+1):
    for j in range(1,C+1):
        if 1<=arr[i][j]<=4: # 온풍기(i,j,dr)
            hlst.append((i,j,arr[i][j]))
        elif arr[i][j] == 5:
            mlst.append((i,j))

# 확산 방향 / 우, 좌, 상, 하
dr_dict = {1:((3,1),(1,),(4,1)), 2:((4,2),(2,),(3,2)), 3:((2,3),(3,),(1,3)), 4:((1,4),(4,),(2,4))}
from collections import deque

def bfs(si,sj,dr):
    q = deque()
    w = [[0] * (C+2) for _ in range(R+2)]

    si,sj = si+di[dr], sj+dj[dr]
    q.append((si,sj,dr))
    w[si][sj] = 5
    v[si][sj] += 5
    while q:
        ci,cj,dr = q.popleft()
        # dr_dict에 들어있는 방향들을 모두 성공해야 확산 가능
        for dirs in dr_dict[dr]:
            si,sj = ci,cj
            if w[ci][cj] == 1: continue

            for dir in dirs:
                ni,nj = si+di[dir],sj+dj[dir]
                # 범위 내이고 현재위치에서 방향으로 벽이 없고
                if 1<=ni<=R and 1<=nj<=C and wall[si][sj][dir] == 0 and w[ni][nj] == 0:
                    si,sj = ni,nj # 현재위치를 시작 방향으로 바꾸고 다음 범위 체크
                else:
                    break
            else: # break 안한건 모든 방향에 만족 (벽 없고, 범위 내, 미방문)
                q.append((ni,nj,dr))
                w[ni][nj] = w[ci][cj] - 1
                v[ni][nj] += w[ni][nj]


v = [[0] * (C+2) for _ in range(R+2)] # 온도 누적할 v[]

for ans in range(1,101):
    # [1] 모든 온풍기 바람 확산 (모든 경로에 벽이 없는 경우 확산, 누적)
    for si, sj, dr in hlst:
        bfs(si,sj,dr)
    # [2] 온도 조절 : 모든 칸 기준 (인접 4방향, 벽이 없는 경우 온도 차이 / 4)
    nv = [x[:] for x in v]
    for i in range(1,R+1):
        for j in range(1,C+1): # 모든 기준 좌표
            for dr in range(1,5): # 네 방향
                if wall[i][j][dr] == 0: # 벽이 없다면
                    ni,nj = i+di[dr], j+dj[dr]
                    if 1<=ni<=R and 1<=nj<=C:
                        val = (v[i][j]-v[ni][nj]) // 4
                        if val > 0:
                            nv[i][j] -= val # 현재 좌표에서 빼기
                            nv[ni][nj] += val # 인접 좌표에서 뺴기
    v = nv
    # [3] 바깥쪽 온도 1 감소(>0)
    for j in range(1,C+1):
        v[1][j] = max(0,v[1][j]-1)
        v[R][j] = max(0,v[R][j]-1)
    for i in range(2,R):
        v[i][1] = max(0,v[i][1]-1)
        v[i][C] = max(0,v[i][C]-1)


    # [4] 조사위치 온도 측정(>=K인 경우 중단)
    for i,j in mlst:
        if v[i][j] < K:
            break
    else:
        break

else:
    ans = 101

print(ans)