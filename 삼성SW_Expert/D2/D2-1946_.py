T = int(input())

for tc in range(1,T+1):
    N = int(input())
    answer = ''
    for i in range(N):
        Ci, Ki = input().split()
        Ki= int(Ki)
        answer += Ci * Ki
    print('#{}'.format(tc))

    for i in range(len(answer)):
        if (i+1)%10 == 0:
            print(answer[i])
        else:
            print(answer[i],end='')
