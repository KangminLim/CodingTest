def is_inrange(x,y):
    return 1<=x and x<=n and 1<=y and y<=n

n,m,p,c,d = map(int,input().split())
rudolf = tuple(map(int,input().split()))

points = [0]*(p+1)
pos = [(0,0)] * (p+1)
board = [[0]*(n+1) for _ in range(n+1)]
is_live = [False] * (p+1)
stun = [0]*(p+1)

dx, dy = [-1,0,1,0], [0,1,0,-1]

board[rudolf[0]][rudolf[1]] = -1

# 맵 정보
for _ in range(p):
    id,x,y = tuple(map(int,input().split()))
    pos[id] = (x,y)
    board[pos[id][0]][pos[id][1]] = id
    is_live[id] = True


for t in range(1,m+1):
    closestX, closestY, closestIdx = 10000, 10000, 0
    # 살아있는 루돌프중에서 가장 가까운 산타 찾기
    for i in range(1,p+1):
        if not is_live[i]:
            continue
        #
        currentBest = ((closestX-rudolf[0])**2 +(closestY-rudolf[1])**2,(-closestX,-closestY))
        currentValue = ((pos[i][0]-rudolf[0])**2 + (pos[i][1]-rudolf[1])**2 , (-pos[i][0], -pos[i][1]))

        if currentValue < currentBest:
            closestX, closestY = pos[i]
            closestIdx = i

    # 가장 가까운 산타의 방향으로 루돌프가 이동
    if closestIdx:
        prevRudolf = rudolf
        moveX = 0
        if closestX > rudolf[0]:
            moveX = 1
        elif closestX < rudolf[0]:
            moveX = -1

        moveY = 0
        if closestY > rudolf[1]:
            moveY = 1
        elif closestY < rudolf[1]:
            moveY = -1

        rudolf = (rudolf[0] + moveX, rudolf[1] + moveY)
        board[prevRudolf[0]][prevRudolf[1]] = 0

    # 루돌프의 이동으로 충돌한 경우, 산타를 이동시키고 처리
    if rudolf[0] == closestX and rudolf[1] == closestY:
        firstX = closestX + moveX * c
        firstY = closestY + moveY * c
        lastX, lastY = firstX, firstY

        stun[closestIdx] = t+1

        # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동이 일어난다.
        while is_inrange(lastX,lastY) and board[lastX][lastY] >0:
            lastX += moveX
            lastY += moveY

        # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
        # 순차적으로 보드판에 있는 산타를 한칸씩 이동
        while not (lastX == firstX and lastY == firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY

            # 위치 벗어나면 루프 끝
            if not is_inrange(beforeX,beforeY):
                break

            idx = board[beforeX][beforeY]

            # 위치 벗어나면 죽음
            if not is_inrange(lastX,lastY):
                is_live[idx]=False
            # 연쇄 충돌
            else:
                board[lastX][lastY] = board[beforeX][beforeY]
                pos[idx]= (lastX,lastY)
            lastX,lastY = beforeX, beforeY

        # 처음 밀린 애가 주인공
        points[closestIdx] += c
        pos[closestIdx] =(firstX, firstY)

        if is_inrange(firstX,firstY):
            board[firstX][firstY] = closestIdx
        else:
            is_live[closestIdx] = False

    board[rudolf[0]][rudolf[1]] = -1

    # 각 산타들은 루돌프와 가장 가까운 방향으로 1씩 이동
    for i in range(1,p+1):
        if not is_live[i] or stun[i] >= t:
            continue

        minDist = (pos[i][0] - rudolf[0])**2 + (pos[i][1] - rudolf[1])**2
        moveDir = -1

        for dir in range(4):
            nx = pos[i][0] + dx[dir]
            ny = pos[i][1] + dy[dir]

            if not is_inrange(nx,ny) or board[nx][ny] >0:
                continue

            dist = (nx - rudolf[0])**2 + (ny - rudolf[1])**2
            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1:
            nx = pos[i][0] + dx[moveDir]
            ny = pos[i][1] + dy[moveDir]

            # 산타의 이동으로 충돌한 경우, 산타를 이동시키고 처리를 한다.
            if nx == rudolf[0] and ny ==rudolf[1]:
                stun[i] = t+1
                moveX = -dx[moveDir]
                moveY = -dy[moveDir]

                firstX = nx + moveX * d
                firstY = ny + moveY * d
                lastX, lastY = firstX, firstY

                if d == 1:
                    points[i] += d

                else:
                    # 만약 이동한 위치에 산타가 있을 경우, 연쇄적으로 이동
                    while is_inrange(lastX,lastY) and board[lastX][lastY] > 0:
                        lastX += moveX
                        lastY += moveY

                    # 연쇄적으로 충돌이 일어난 가장 마지막 위치에서 시작해,
                    # 순차적으로 보드판에 있는 산타를 한칸씩 이동
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not is_inrange(beforeX,beforeY):
                            break

                        idx = board[beforeX][beforeY]

                        if not is_inrange(lastX, lastY):
                            is_live[idx] = False

                        else:
                            board[lastX][lastY] = board[beforeX][beforeY]
                            pos[idx] = (lastX, lastY)
                        lastX, lastY = beforeX, beforeY

                    points[i] += d
                    board[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX,firstY)

                    if is_inrange(firstX, firstY):
                        board[firstX][firstY] = 1
                    else:
                        is_live[i] = False
            else:
                board[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx,ny)
                board[nx][ny] = i

    for i in range(1, p+1):
        if is_live[i]:
            points[i] += 1

for i in range(1, p+1):
    print(points[i], end=" ")

















