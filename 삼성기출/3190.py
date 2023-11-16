N = int(input())
K = int(input())
alst = [tuple(map(int,input().split())) for _ in range(K)]
L = int(input())
dlst = [input().split() for _ in range(L)]
dtbl =[0] * (10001) # 방향전화에 사용
for sec, turn in dlst:
    dtbl[int(sec)] = turn

di, dj = [-1,0,1,0], [0,1,0,-1] # 시계방향으로 방향정의
dr = 1  #오른쪽 방향
snake=[(1,1)] # 좌측상단
ans=0 # 0초

while True:
    ans +=1  # 1초 경과
    ci,cj = snake[0] # 현재 머리좌표
    ni,nj = ci+di[dr], cj+dj[dr] # 진행방향으로 한칸 이도
    # 벽에 부딪혔거나, 뱀 몸에 부딪힌 경우 종료
    if 1<=ni<=N and 1<=nj<=N and (ni,nj) not in snake:
        snake.insert(0,(ni,nj)) # 머리위치[0]에 이동좌표 확장
        if (ni,nj) in alst: # 사과가 있다면
            alst.remove((ni,nj))
        else:
            snake.remove((snake[-1])) # 꼬리부분 제거
        if dtbl[ans] == 'D':
            dr =(dr+1)%4
        elif dtbl[ans] == 'L':
            dr = (dr+3)%4
    else:
        break
print(ans)