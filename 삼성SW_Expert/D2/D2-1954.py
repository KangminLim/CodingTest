T = int(input())
# row, col 인덱스로 탐색할 수 있게 방향 설정(달팽이 방향이니까 우->하->좌->상)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    lst = [[0]*N for _ in range(N)]
    # 초기 위치 & 회전방향 설정
    r, c = 0, 0
    dist = 0 # 0:우, 1:하, 2:좌, 3:우

    for n in range(1,N*N+1):
        lst[r][c] = n
        r += dr[dist]
        c += dc[dist]

        if r<0 or c<0 or r>=N or c>=N or lst[r][c] != 0:
            # 실행취소
            r -= dr[dist]
            c -= dc[dist]
            # dist 나머지값으로 계산  -> 값이 커져서 이용하지 못하므로
            dist = (dist + 1) % 4

            r += dr[dist]
            c += dc[dist]

    print("#{}".format(tc))
    for row in lst:
        print(*row)
