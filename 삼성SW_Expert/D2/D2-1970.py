T = int(input())
won = [50000,10000,5000,1000,500,100,50,10]

for tc in range(1,T+1):
    N = int(input())
    print('#{}'.format(tc))
    lst = [0] * 8
    for i in range(8):
        if (N//won[i]) != 0:
            lst[i] = (N//won[i])
            N = N - won[i]*lst[i]

    print(*lst)