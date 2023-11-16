for _ in range(10):
    tc = int(input())
    S = list(map(int,input().split()))
    tc_list = [10,6,12,8,9,4,1,3]
    while(S[-1] > 0):
        for i in range(1,6):
            if S[0]-i>0:
                S.append(S[0]-i)
                S.pop(0)
            else:
                S.append(0)
                S.pop(0)
                break
    print('#{}'.format(tc),end=' ')
    print(*S)
