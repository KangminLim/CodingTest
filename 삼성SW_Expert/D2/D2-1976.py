T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    print(puzzle)
    answer=0
    # 행
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count +=1
            # 마지막 열
            if puzzle[i][j] == 0 or j == N-1 :
                if count == K:
                    answer += 1
                if puzzle[i][j] == 0:
                    count = 0
    # 열
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                count += 1
            if puzzle[j][i] == 0 or j == N-1:
                if count == K:
                    answer += 1
                if puzzle[j][i] == 0:
                    count =0
    print('#{} {}'.format(tc,answer))