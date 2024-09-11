N, M, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
turn = [[(0,0)] * N for _ in range(N)]
ddict = {}

player = {}
dr = list(map(lambda x: int(x)-1,input().split()))
for m in range(M):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == m+1:
                player[m+1] = [i,j,dr[m]]
                turn[i][j] = (K,m+1)
for m in range(1,M+1):
    ddict[m] = {}
    for k in range(4):
        a, b, c, d = map(lambda x:int(x)-1,input().split())
        ddict[m][k] = [a,b,c,d]

di,dj = [-1,1,0,0], [0,0,-1,1]

mflag = True
T = 0
while len(player) > 1 and T <= 1000:
    T += 1
    if T == 1001:
        mflag = False
        break
    narr = [x[:] for x in arr]
    nturn = [x[:] for x in turn]
    for idx in player:
        ci,cj,cd = player[idx]
        flag = True
        for k in range(4):
            nd = ddict[idx][(cd+k)%4]
            # 독점계약 맺지 않은 칸 있는지 확인
            for dr in nd:
                ni,nj = ci+di[dr], cj+dj[dr]
                if 0<=ni<N and 0<=nj<N and ((turn[ni][nj][1]>0 and turn[ni][nj][0] < T) or not turn[ni][nj][1]):
                    # nturn[ni][nj] = (T+K,idx)
                    player[idx] = [ni,nj,dr]
                    # narr[ni][nj] = idx
                    narr[ci][cj] = 0
                    flag = False
                    break
            # 이동을 한 것
            if not flag:
                break

        # 본인이 독점 계약한 땅으로 이동
        if flag:
           tflag = True
           for k in range(4):
               nd = ddict[idx][(cd + k) % 4]
               # 본인이 독점 계약한 땅으로 이동
               for dr in nd:
                   ni, nj = ci + di[dr], cj + dj[dr]
                   if 0 <= ni < N and 0 <= nj < N and turn[ni][nj][1] == idx:
                       # nturn[ni][nj] = (T + K, idx)
                       player[idx] = [ni, nj, dr]
                       # narr[ni][nj] = idx
                       narr[ci][cj] = 0
                       tflag = False
                       break
               # 이동을 한 것
               if not tflag:
                   break


    i,M = sorted(player.keys())[0], sorted(player.keys())[-1]
    tset = set()
    while i<M:
        if i not in player:
            i += 1
            continue
        ci,cj,cd = player[i]
        for j in range(i+1,M+1):
            if j not in player: continue

            ti,tj,td = player[j]
            if (ci,cj) == (ti,tj):
                tset.add(j)
                if j == M:
                    break
        i += 1

    if tset:
        for n in tset:
            player.pop(n)


    for idx in player:
        ci,cj,cd = player[idx]
        nturn[ci][cj] = (T + K, idx)
        narr[ci][cj] = idx

    turn = nturn
    arr = narr
if not mflag:
    print(-1)
else:
    print(T)