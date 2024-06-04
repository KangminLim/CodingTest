import sys 
input = sys.stdin.readline

N = int(input())
lst = [list(map(str,input().split())) for _ in range(N)]
teachers, spaces = [], []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'T':
            teachers.append((i,j))
        elif lst[i][j] == 'X':
            spaces.append((i,j))

from itertools import combinations
di,dj = [-1,1,0,0], [0,0,-1,1]
# 2. check 함수
def student_check(ti,tj):
    # 선생님의 위치에서 상하좌우로 한칸씩 점진적으로 검사
    for dr in range(4):
        ni,nj = ti+di[dr], tj+dj[dr]

        while 0<=ni<N and 0<=nj<N and lst[ni][nj] != 'O':
            # 장애물을 만나지 않고 학생을 만나면 False
            if lst[ni][nj] == 'S':
                return False
            ni += di[dr]
            nj += dj[dr]
    return True

# 1. 빈칸 중 3 공간에 장애물 설치
find = False
for comb in combinations(spaces,3):
    cnt = 0
    for ci,cj in comb:
        lst[ci][cj] = 'O' # 장애물 설치

    for ti, tj in teachers:
        if student_check(ti,tj):
            cnt += 1
        else:
            break

    if cnt == len(teachers):
        find = True
        break

    for ci, cj in comb:
        lst[ci][cj] = 'X'

if find:
    print('YES')
else:
    print('NO')