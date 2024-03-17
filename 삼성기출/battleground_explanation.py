EMPTY = (-1,-1,-1,-1,-1,-1)

# 변수 선언 및 입력
n, m, k = tuple(map(int,input().split()))

# 각 칸마다 놓여있는 총 목록을 관리합니다.
gun = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    nums = list(map(int,input().split()))
    for j in range(n):
        # 총이 놓여 있는 칸
        if nums[j] != 0:
            gun[i][j].append(nums[j])

# 각 칸마다 플레이어 정보를 관리
# 순서대로 (num, x, y, d, s, a) 정보를 관리
# (x,y) 위치에서 방향 d를 보ㅗㄱ 있으며
# 초기 능력치가 s인 num번 플레이어가
# 공격력 a인 총을 들고 있음을 뜻한다.
# 총이 없으면 a는 0이다.

players = []
for i in range(m):
    x, y, d, s = tuple(map(int,input().split()))
    players.append((i, x-1, y-1, d, s, 0))

# dx dy
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

points = [0] * m

def is_range(x,y):
    return 0 <= x < n and 0<=y<n

# 1. 현재 (x,y)위치에서 방향 d를 보고 있을 때 그 다음 위치와 방향을 찾아줌
def get_next(x,y,d):
    nx, ny = x+dx[d], y +dy[d]
    if not is_range(nx,ny):
        # 반대 방향
        if d < 2:
            d += 2
        else:
            d -= 2
        nx, ny = x +dx[d], y +dy[d]
    return (nx,ny,d)
# 2-1 이동한 칸에 플레이어 찾기 / 없다면 EMPTY 반환
def find_player(pos):
    for i in range(m):
        x, y= players[i][1], players[i][2]
        if pos == (x,y):
            return players[i]
    return EMPTY

# player p의 정보를 갱신
def update(p):
    num, _,_,_,_,_ = p

    for i in range(m):
        num_i,_,_,_,_,_ =players[i]
        if num_i == num:
            players[i] = p
            break

# 플레이어 p를 pos 위치로 이동시킨다.
def move(p, pos):
    num,x,y,d,s,a = p
    nx, ny = pos

    # 가장 좋은 총으로 변경
    gun[nx][ny].append(a)
    gun[nx][ny].sort(reverse=True)
    a = gun[nx][ny][0]
    gun[nx][ny].pop(0)

    p = (num,nx,ny,d,s,a)
    update(p)

# 패배한 플레이어
def loser_move(p):
    num, x, y, d, s, a = p
    # 먼저 현재 위치에 총을 내려놓게 된다.
    gun[x][y].append(a)

    # 빈 공간을 찾아 90도 회전
    for i in range(4):
        ndir = (d+i) % 4
        nx, ny = x + dx[ndir] , y + dy[ndir]
        if is_range(nx,ny) and find_player((nx,ny)) == EMPTY:
            p = (num, x, y, ndir, s, 0)
            move(p, (nx,ny))
            break

def duel(p1,p2,pos):
    num1, _, _ ,d1,s1,a1 = p1
    num2, _, _, d2,s2,a2 = p2

    # (초기 능력치 + 총의 공격력, 초기 능력치) 순으로

    # p1 승리
    if (s1+a1, s1) > (s2+a2, s2):
        points[num1] += (s1+a1) - (s2+a2)
        loser_move(p2)
        move(p1,pos)
    # p2 승리
    else:
        points[num2] += (s2+a2) - (s1+a1)
        loser_move(p1)
        move(p2,pos)

def simulate():
    for i in range(m):

        num, x, y, d, s, a = players[i]
        # 현재 플레이어가 움직일 그 다음 위치와 방향 구하기
        nx,ny,ndir = get_next(x,y,d)
        # 해당 위치에 있는 전 플레이어 정보를 가져온다
        next_player = find_player((nx,ny))
        # 현재 플레이어의 위치와 방향을 보정
        cur_player = (num,nx,ny,ndir,s,a)
        update(cur_player)

        if next_player == EMPTY:
            move(cur_player, (nx,ny))
        else:
            duel(cur_player, next_player, (nx,ny))

for _ in range(k):
    simulate()

for point in points:
    print(point, end=' ')












