N, M, hp = map(int,input().split())
arr = [[-1] * (N+2)] + [[-1] + list(map(int,input().split())) + [-1] for _ in range(N)] + [[-1] * (N+2)]

# 벽 -1로 변경
for i in range(1,N+1):
    for j in range(1,N+1):
        if arr[i][j] == 1:
            arr[i][j] = -1

ti, tj = map(int,input().split())

sset = set()
ddict = {}

for idx in range(1,M+1):
    si,sj,ei,ej = map(int,input().split())
    arr[si][sj] = idx
    sset.add((si,sj))
    ddict[idx] = (ei,ej)
flag = True # 이동 불가 플래그

from collections import deque
def find(si,sj,dest):
    q = deque()
    q.append((si,sj,0))
    v = [[False] * (N+2) for _ in range(N+2)]
    v[si][sj] = True
    cnt = 0
    while q:
        tlst = []
        nq = deque()
        cnt += 1
        for ci, cj, m in q:
            if (ci,cj) in dest:
                tlst.append((m,ci,cj))
            else:
                for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                    if arr[ni][nj] >= 0 and not v[ni][nj]:
                        nq.append((ni,nj,cnt))
                        v[ni][nj] = True
        q = nq
        if tlst:
            return sorted(tlst)[0]

    return False

while ddict:
    # 가장 가까운 승객 찾기
    if not find(ti,tj,sset):
        flag = False
        break
    else:
        cnt,ni,nj = find(ti,tj,sset)
    # 승객 리스트 제거
    sset.remove((ni,nj))
    # 종료 조건 (배터리 0 되면 종료)
    if hp - cnt < 0:
        flag = False
        break
    hp -= cnt
    # 승객에 따른 도착 지점 리스트
    tdi, tdj = ddict[arr[ni][nj]]
    ddict.pop(arr[ni][nj])
    # 택시가 승객을 목적지로 무사히 태워주면
    if not find(ni,nj,set(((tdi,tdj),(0,0)))):
        flag = False
        break
    else:
        cnt,ei,ej = find(ni,nj,set(((tdi,tdj),(0,0))))

    # 종료 조건 (배터리 0 되면 종료)
    if hp - cnt < 0:
        flag = False
        break

    hp += cnt

    ti,tj = ei, ej

if flag:
    print(hp)
else:
    print(-1)