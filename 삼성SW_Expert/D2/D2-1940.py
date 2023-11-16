T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cur_speed = 0
    answer = 0
    for i in range(N):
        arr = list(map(int,input().split()))
        if arr[0] == 0:
            if i==0:
                continue
            else:
                answer += cur_speed
        elif arr[0] == 1:
            cur_speed += arr[1]
            answer += cur_speed
        else:
            if cur_speed < arr[1]:
                cur_speed=0
                continue
            cur_speed -= arr[1]
            answer += cur_speed
    print('#{} {}'.format(tc,answer))