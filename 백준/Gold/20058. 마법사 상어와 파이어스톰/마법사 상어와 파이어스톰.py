N, Q = map(int,input().split())
N = 2**N

arr =  [[0] * (N+2)] + [[0] + list(map(int,input().split()))  + [0] for _ in range(N)] + [[0] * (N+2)]
lst = list(map(int,input().split()))
for L in lst: # Q번 시전할 부분 격자 크기 순차 처리
    L = 2**L # (부분 격자) 한 변 크기 저장

    # [1] 부분 격자를 시계방향 90도 회전
    new = [[0] * (N+2) for _ in range(N+2)]
    for si in range(1,N+1,L):
        for sj in range(1,N+1,L): # 가능한 모든 기준
            for i in range(L):
                for j in range(L):
                    new[si+i][sj+j] = arr[si+L-1-j][sj+i]

    arr = new

    # [2] 네방향, 0이 2개 이상이면 얼음 -1 감소
    new = [x[:] for x in arr] # arr을 deepcopy
    for i in range(1,N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0 : continue # 얼음이 아니면 skip

            cnt = 0
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                if arr[i+di][j+dj] == 0: # 얼음이 아니면
                    cnt += 1
                    if cnt >= 2:
                        new[i][j] -= 1
                        break

    arr = new

def bfs(si,sj):
    q = []

    q.append((si,sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.pop(0)
        # 네방향, 미방문, **조건: 얼음이면(>0)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if v[ni][nj] == 0 and arr[ni][nj] >0:
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt

# [3] 정답처리 : 남은 얼음덩어리 중 가장 큰 크기
v = [[0] * (N+2) for _ in range(N+2)]
ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if v[i][j] == 0 and arr[i][j] >0 : # 미방문 어음이면
            ans = max(ans,bfs(i,j))

print(sum(map(sum,arr)))
print(ans)