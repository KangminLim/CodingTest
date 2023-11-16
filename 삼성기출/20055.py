N,K = map(int,input().split())
lst= list(map(int,input().split()))
robot =[0]*N
ans = 0
while True:
    ans += 1
    # [1] 벨트, 로봇회전 + [N-1]로봇 내림
    lst = [lst[-1]] + lst[:-1]
    robot =[0]+ robot[:-1]

    # [2] 먼저 올라간 로봇부터 처리
    for i in range(N-2,0,-1):
        if robot[i]==1 and robot[i+1]==0 and lst[i+1]>0:
            robot[i], robot[i+1]=0,1
            lst[i+1]-=1
    # [3] 0자리 내구도 >0이면 로봇 올림
    if lst[0]>0:
        robot[0]=1
        lst[0]-=1

    # [4] 0인 개수 >= K이면 탈출
    if lst.count(0)>=K:
        break
print(ans)