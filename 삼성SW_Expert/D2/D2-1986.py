T = int(input())

for tc in range(1,T+1):
    N = int(input())
    result = []
    result_sum = 0
    for i in range(1,N+1):
        if i%2==0:
            result_sum -= i
        else:
            result_sum += i
    print('#{} {}'.format(tc,result_sum))