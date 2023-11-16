for tc in range(10):
    N = int(input())
    S = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(0,8-N+1):
            if S[i][j:j+N] == S[i][j:j+N][::-1]:
                cnt+=1
    # 전치행렬
    S = list(zip(*S))
    # print(S)
    for i in range(8):
        for j in range(0,8-N+1):
            if S[i][j:j + N] == S[i][j:j + N][::-1]:
                cnt += 1
    print('#{} {}'.format(tc+1,cnt))



