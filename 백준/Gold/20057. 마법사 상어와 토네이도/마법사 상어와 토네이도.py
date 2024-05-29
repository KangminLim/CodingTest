N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

mul = [2,10,7,1,5,10,7,1,2,0] # % 비율
ai = [[-2,-1,-1,-1,0,1,1,1,2,0],
    [0,1,0,-1,2,1,0,-1,0,1],
    [2,1,1,1,0,-1,-1,-1,-2,0],
    [0,-1,0,1,-2,-1,0,1,0,-1]]
aj = [[0,-1,0,1,-2,-1,0,1,0,-1],
    [-2,-1,-1,-1,0,1,1,1,2,0],
    [0,1,0,-1,2,1,0,-1,0,1],
    [2,1,1,1,0,-1,-1,-1,-2,0]]

ti,tj,td = N//2,N//2,0
tdi,tdj = [0,1,0,-1],[-1,0,1,0]
mx_cnt,cnt,flag= 1,0,0
ans = 0

while (ti,tj) != (0,0):

    ti,tj = ti+tdi[td],tj+tdj[td]

    # [1] ti,tj 기준 좌표 중심으로 모래량 계산 추가, 범위밖 => ans 추가
    if arr[ti][tj] > 0: # 모래가 있을때만 진행
        val = arr[ti][tj] # 기준좌표 모래양
        arr[ti][tj] = sm = 0 # 기준좌표 모래는 날라가서 없어짐

        for i in range(10): # 위치 0~9까지 처리
            ni,nj = ti+ai[td][i],tj+aj[td][i] # 좌표 계산
            t = (val*mul[i])//100 # 소수점 이하 버림
            if i==9: # 나머지 모래
                t = val - sm


            if 0<=ni<N and 0<=nj<N: # 범위 내 => 누적
                arr[ni][nj] += t
            else:
                ans += t # 밖으로 나간 모래양에 추가
            sm += t

    cnt += 1

    if mx_cnt == cnt:
        cnt = 0
        td = (td+1)%4

        if flag == 0:
            flag = 1
        else:
            flag = 0
            mx_cnt += 1


print(ans)