from collections import deque
n = int(input())
mp = []
visited = [[False] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 그룹의 개수
group_n =0
# 각 칸에 그룹 번호 적기
group = [[0] * n for _ in range(n)]
group_cnt = [0] * (n*n+1)
next_arr = [[0] * n for _ in range(n)]

for _ in range(n):
    mp.append(list(map(int,input().split())))

def is_range(x,y):
    return 0<=x<n and 0<=y<n


def bfs(i,j):
    global group_n
    q = deque()
    q.append((i,j))
    visited[i][j] = True
    group[i][j] = group_n
    group_cnt[group_n] = 1
    while q:
        x, y = q.popleft()
        for dr in range(4):
            nx = x + dx[dr]
            ny = y + dy[dr]
            if is_range(nx,ny) and not visited[nx][ny] and mp[nx][ny] == mp[x][y]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    group[nx][ny] = group_n
                    group_cnt[group_n] += 1

def make_group():
    global group_n
    # visited 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_n += 1
                bfs(i,j)

def get_art_score():
    art_score = 0

    for i in range(n):
        for j in range(n):
            for dr in range(4):
                nx, ny = i+dx[dr], j+dy[dr]
                if is_range(nx,ny) and mp[i][j] != mp[nx][ny]:
                    g1, g2 = group[i][j], group[nx][ny]
                    num1, num2 = mp[i][j], mp[nx][ny]
                    cnt1, cnt2 = group_cnt[g1], group_cnt[g2]

                    art_score += (cnt1+cnt2) * num1 * num2
    return art_score // 2

def get_score():
    # 2.1 그룹 형성
    make_group()

    # 2.2 예술 점수 계산
    return get_art_score()

# 정사각형 시계방향 90도 회전
def rotate_square(sx, sy, square_n):
    for x in range(sx, sx+square_n):
        for y in range(sy, sy+square_n):
            ox, oy = x - sx, y - sy
            rx, ry = oy, square_n-ox-1
            next_arr[rx+sx][ry+sy] = mp[x][y]

def rotate():
    # next_arr 초기화
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0

    # 회전 진행
    # 십자 모양 반시계 방향 회전
    for i in range(n):
        for j in range(n):
            # 세로 (i,j) -> (j,i)
            if j == n//2:
                next_arr[j][i] = mp[i][j]
            # 가로 (i,j) -> (n-j-1,i)
            elif i == n//2:
                next_arr[n-j-1][i] = mp[i][j]

    square_n = n//2
    rotate_square(0, 0, square_n)
    rotate_square(0, square_n + 1, square_n)
    rotate_square(square_n + 1, 0, square_n)
    rotate_square(square_n + 1, square_n + 1, square_n)

    for i in range(n):
        for j in range(n):
            mp[i][j] = next_arr[i][j]
ans = 0

for _ in range(4):
    ans += get_score()
    rotate()

print(ans)

