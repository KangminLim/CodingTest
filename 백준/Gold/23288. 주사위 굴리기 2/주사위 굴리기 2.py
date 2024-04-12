N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 시계 : 상, 우, 하, 좌
di , dj = [-1,0,1,0], [0,1,0,-1]
d1,d2,d3,d4,d5,d6= 1,2,3,4,5,6
dr =1
ci,cj = 0,0
ans = 0
def bfs(si,sj,val):
    q = []
    v = [[0] * M for _ in range(N)]

    q.append((si,sj))
    v[si][sj] =1
    cnt = 1

    while q:
        ci,cj = q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not v[ni][nj] and arr[ni][nj]==val:
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt

for _ in range(K): # k번 이동
    # [1] 한칸 이동(dr), 범위 밖 => 방향을 반대로
    ni,nj = ci+di[dr], cj+dj[dr]
    if 0<=ni<N and 0<=nj<M:
        ci,cj = ni,nj
    else: # 범위 밖 => 반대 방향 이동
        dr = (dr+2)%4
        ci,cj = ci+di[dr], cj+dj[dr]
    # [1] 좌표의 이동처럼, 주사위 회전도 처리
    if dr == 0: # 상(북)
        d2,d1,d5,d6 = d1,d5,d6,d2
    elif dr == 1: # 우(동)
        d6,d4,d1,d3 = d3,d6,d4,d1
    elif dr == 2: # 하(남)
        d2,d1,d5,d6 = d6,d2,d1,d5
    else:
        d6,d4,d1,d3 = d4,d1,d3,d6

    # [2] 점수계산 : arr[] 같은 값 이면 그 개수 만큼 점수
    ans += bfs(ci,cj,arr[ci][cj])*arr[ci][cj]

    # [3] 주사위 방향 전환
    if d6 > arr[ci][cj] : dr=(dr+1)%4 # 시계방향
    elif d6 <  arr[ci][cj]: dr=(dr-1)%4 # 반시계 방향

print(ans)