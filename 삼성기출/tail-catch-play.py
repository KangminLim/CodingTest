from collections import deque
n,m,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

groups = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            w = deque([(i,j)])
            e = deque([(i, j)])
            while w:
                x, y = w.popleft()
                for k in range(4):
                    nx,ny = x+dx[k], y+dy[k]

                    if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 2 and (nx,ny) not in e:
                        e.append((nx,ny))
                        w.append((nx,ny))
            x, y =e[-1][0], e[-1][1]
            for k in range(4):
                nx, ny = x + dx[k], y+dy[k]
                if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 3:
                    e.append((nx,ny))
                    break
            groups.append(e)

def move():
    for group in groups:
        x,y = group.pop() # 꼬리 만들기
        arr[x][y] = 4 # 선로로 돌리기
        arr[group[-1][0]][group[-1][1]] = 3 # 새로운 꼬리

        x,y = group[0]
        arr[x][y] = 2 # 머리를 몸통으로
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 4:
                arr[nx][ny] = 1
                group.appendleft((nx,ny))
                break

def ball(round): # return은 (-1,-1) 즉 좌표로 해서, 큐에 접근하여 뒤바꿀 기차와 점수 알아내기
    round %=4*n
    if round < n:
        for j in range(n):
            if arr[round][j] in (1,2,3): return (round,j)
    elif round < 2*n:
        for i in range(n):
            if arr[n-1-i][round-n] in (1,2,3): return (n-1-i,round-n)
    elif round < 3*n:
        for j in range(n):
            if arr[3*n-1-round][n-1-j] in (1,2,3): return (3*n-1-round,n-1-j)
    else:
        for i in range(n):
            if arr[i][4*n-1-round] in (1,2,3): return (i,4*n-1-round)
    return (-1,-1)

def change(x,y):
    if (x,y) == (-1,-1): return 0

    for i in range(m):
        if (x,y) in groups[i]:
            for j in range(len(groups[i])):
                if groups[i][j] == (x,y):
                    arr[groups[i][0][0]][groups[i][0][1]] = 3
                    arr[groups[i][-1][0]][groups[i][-1][1]] = 1
                    groups[i].reverse()
                    return (j+1) ** 2
cnt = 0

for i in range(K):
    move()
    a,b = ball(i)
    cnt += change(a,b)
print(cnt)


