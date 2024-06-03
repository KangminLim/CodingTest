from itertools import combinations
N = int(input())
spaces, teachers, data = [], [], []


for i in range(N):
    data.append(list(input().split()))
    for j in range(N):
        if data[i][j] == 'T':
            teachers.append((i,j))
        if data[i][j] == 'X':
            spaces.append((i,j))

def watch(x,y,direction):
    # 왼쪽감시
    if direction == 0:
        while y >= 0:
            if data[x][y] == 'S': #학생이 있는 경우
                return True
            if data[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽감시
    if direction == 1:
        while y < N:
            if data[x][y] == 'S': #학생이 있는 경우
                return True
            if data[x][y] == 'O':
                return False
            y += 1
    # 위쪽감시
    if direction == 2:
        while x >= 0:
            if data[x][y] == 'S': #학생이 있는 경우
                return True
            if data[x][y] == 'O':
                return False
            x -= 1
    # 아래쪽감시
    if direction == 3:
        while x < N:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

find = False

for temp in combinations(spaces,3):
    for x, y in temp:
        data[x][y] = 'O'
    if not process():
        find = True
        break
    for x, y  in temp:
        data[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')