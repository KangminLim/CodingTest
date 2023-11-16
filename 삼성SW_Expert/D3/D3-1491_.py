T = int(input())

for tc in range(1,T+1):
    min_value = -1
    N, A, B=map(int,input().split())
    for R in range(1, N+1):
        C = 1
        while(N >= R*C):
            S = A * (abs(R-C)) + B *(N-R*C)
            if min_value == -1:
                min_value = S
            else :
                min_value = min(min_value,S)
            C += 1
    print('#{} {}'.format(tc, min_value))
