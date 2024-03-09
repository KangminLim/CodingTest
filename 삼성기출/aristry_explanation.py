n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
next_arr = [[0] * n for _ in range(n)]

# 그룹의 개수
group_n = 0

# 각 칸에 그룹 번호 적기
group = [[0] * n for _ in range(n)]
group_cnt = [0] * (n*n+1)
visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 1. 그룹 만들기 함수
# 1.1 범위
def is_range(x,y):
    return 0<=x<n and 0<=y<n
# 1.2 dfs 그룹 만들기와 각 그룹의 칸의 수 구학기
def dfs(x,y):
    for dr in range(4):
        nx = x + dx[dr]
        ny = y + dy[dr]
        # 인접한 칸 중에서 숫자가 동일하면서 방문한 적 없는 칸으로만 이동
        if is_range(nx,ny) and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_cnt[group_n] += 1
            dfs(nx,ny)

# 1.3 그룹 만들기 함수
def make_group():
    global group_n
    group_n = 0

    # visited 값을 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    # DFS를 이용하여 그룹 묶는 작업 진행
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                visited[i][j] = True
                group[i][j] = group_n
                group_cnt[group_n] = 1
                dfs(i,j)
# 2. 예술 점수
def get_art_score():
    art_score = 0
    #(a칸의 수 + b칸의 수) * a값 * b값
    for i in range(n):
        for j in range(n):
            for dr in range(4):
                nx, ny = i + dx[dr], j + dy[dr]
                if is_range(nx,ny) and arr[i][j] != arr[nx][ny]:
                    g1, g2 = group[i][j], group[nx][ny]
                    num1, num2 = arr[i][j], arr[nx][ny]
                    cnt1, cnt2 = group_cnt[g1], group_cnt[g2]

                    art_score += (cnt1+cnt2) * num1 * num2
    # 중복 계산 제외
    return art_score // 2

def get_score():
    # 2.1 그룹 형성
    make_group()

    # 2.2 예술 점수 계산
    return get_art_score()

def rotate_square(sx, sy, square_n):
    # 정사각형 90도 회전
    for x in range(sx,sx+square_n):
        for y in range(sy,sy+square_n):
            ox, oy = x-sx, y-sy
            rx, ry = oy, square_n-ox-1
            next_arr[rx+sx][ry+sy] = arr[x][y]

def rotate():
    # next_arr 초기화
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0

    # 3. 회전 진행
    # 3.1 십자 모양 반시계 방향 회전
    for i in range(n):
        for j in range(n):
            # 세로 (i,j) -> (j, i)
            if j == n//2:
                next_arr[j][i] = arr[i][j]
            # 가로 (i,j) -> (n-j-1,i)
            elif i == n//2:
                next_arr[n-j-1][i] = arr[i][j]
    # 3.2 4개의 정사각형에 대해서 시계방향 회전
    square_n = n // 2
    rotate_square(0,0,square_n)
    rotate_square(0,square_n+1,square_n)
    rotate_square(square_n+1,0,square_n)
    rotate_square(square_n+1,square_n+1,square_n)

    # 3.3 next_arr값 다시 옮기기

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

ans = 0
for _ in range(4):
    # 예술 점수 더하기
    ans += get_score()

    rotate()

print(ans)