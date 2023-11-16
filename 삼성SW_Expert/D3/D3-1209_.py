for _ in range(10):
    tc = int(input())
    lst = [list(map(int,input().split())) for _ in range(100)]

    # 가로줄
    max_1 = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += lst[i][j]
        if sum > max_1:
            max_1 = sum

    # 세로줄
    max_2 =0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += lst[j][i]
        if sum > max_2:
            max_2 = sum

    # 대각선
    max_3 = 0
    for i in range(100):
        sum1,sum2=0,0
        sum1 += lst[i][i]
        sum2 += lst[i][99-i]
    if max(sum1,sum2)>max_3:
        max_3 = max(sum1,sum2)

    print('#{} {}'.format(tc,max(max_1,max_2,max_3)))