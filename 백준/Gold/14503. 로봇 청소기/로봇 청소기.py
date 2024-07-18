N, M = map(int,input().split())
ri,rj,rd = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
di,dj = [-1,0,1,0], [0,1,0,-1]
opp = {0:2,1:3,2:0,3:1}
ans = 1
flag = False

while True:
    arr[ri][rj] = 2
    # 4방향 중 빈칸이 있으면
    if arr[ri-1][rj] == 0 or arr[ri][rj+1] == 0 or arr[ri+1][rj] == 0 or arr[ri][rj-1] == 0:
        rd = (rd+3)%4
        if arr[ri+di[rd]][rj+dj[rd]] == 0:
            ri,rj = ri+di[rd],rj+dj[rd]
            ans += 1

    else: # 4방향 중 빈칸이 없으면
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면
        if arr[ri+di[opp[rd]]][rj+dj[opp[rd]]] == 2:
            ri,rj = ri+di[opp[rd]], rj+dj[opp[rd]]
        else:
            flag = True
            break
    if flag:
        break
print(ans)