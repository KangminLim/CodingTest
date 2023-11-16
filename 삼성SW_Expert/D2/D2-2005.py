T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    print('#{}'.format(test_case))
    pascal = [[0] * row for row in range(1,N+1)]
    for i in range(N):
        pascal[i][0] = 1
        pascal[i][-1] =1
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1]+ pascal[i-1][j]
    for i in pascal:
        print(*i)
