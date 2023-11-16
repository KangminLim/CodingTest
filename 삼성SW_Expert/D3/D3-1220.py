T=10
for tc in range(1,11):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    cnt = 0
    for c in range(N):
        isRed =False
        for r in range(N):
            if arr[r][c] == 1:
                isRed=True
            if arr[r][c] == 2 and isRed:
                cnt += 1
                isRed =False
    print(f'#{tc} {cnt}')