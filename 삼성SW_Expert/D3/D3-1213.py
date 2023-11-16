
for a in range(1,11):
    tc =int(input())
    S = str(input())
    len_S = len(S)
    TC = str(input())
    answer = 0
    for i in range(len(TC)):
        # print(TC[i:i+2])
        if S == TC[i:i+len_S]:
            answer += 1

    print('#{} {}'.format(tc,answer))
