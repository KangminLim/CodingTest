T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cur_N = N
    s =set()
    cnt = 1
    while True:
        for k in list(str(cur_N)):
            s.add(k)
        if len(s) == 10:
            break
        cur_N //= cnt
        cnt += 1
        cur_N *= cnt
    print('#{}'.format(tc),end=' ')
    print(cur_N,end=' ')
    print()