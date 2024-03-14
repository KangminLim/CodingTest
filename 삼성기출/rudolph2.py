n, m, p, c, d = map(int,input().split())
rudolf = tuple(map(int,input().split()))
points = [0 for _ in range(p+1)]
pos = [(0,0) for _ in range(p+1)]
is_live = [False for _ in range(p+1)]
stun = [0 for _ in range(p+1)]
graph = [[0] * (n+1) for _ in range(n+1)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def is_inrange(x,y):
    return 1<=x<=n and 1<=y<=n

for _ in range(p):
    id, x, y = tuple(map(int,input().split()))
    pos[id] = (x,y)
    graph[pos[id][0]][pos[id][1]] = id
    is_live[id] = True

for t in range(1,m+1):
    closestX, closestY, closestIdx = 10000, 10000, 0

    # 1. 루돌프 움직임
    # 1.1.1 가장 가까운 산타 찾기
    for i in range(1,p+1):
        if not is_live[i]:
            continue

        curBest = ((closestX-rudolf[0])**2 + (closestY-rudolf[1])**2,(-closestX,-closestY))
        curValue = ((pos[i][0]-rudolf[0])**2 + (pos[i][1]-rudolf[1])**2,(-pos[i][0],-pos[i][1]))

        if curValue < curBest:
            closestX, closestY = pos[i]
            closestIdx = i

    # 1.1.2 가장 가까운 산타의 방향으로 이동
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
        graph[prevRudolf[0]][prevRudolf[1]] = 0

    # 1.2 루돌프 이동에 의한 충돌
    if rudolf[0] == closestX and rudolf[1] == closestY:
        firstX = closestX + moveX * c
        firstY = closestY + moveY * c
        lastX, lastY = firstX, firstY

        stun[closestIdx] = t+1

        # 1.3 루돌프 이동에 의한 상호작용 (마지막 위치까지)
        while is_inrange(lastX, lastY) and graph[lastX][lastY] > 0:
            lastX += moveX
            lastY += moveY

        while not (lastX==firstX and lastY==firstY):
            beforeX = lastX - moveX
            beforeY = lastY - moveY

            if not is_inrange(beforeX, beforeY):
                break

            idx = graph[beforeX][beforeY]

            # 생존 처리
            if not is_inrange(lastX, lastY):
                is_live[idx] = False
            else:
                graph[lastX][lastY] = graph[beforeX][beforeY]
                pos[idx] = (lastX, lastY)

            lastX, lastY = beforeX, beforeY

        points[closestIdx] += c
        pos[closestIdx] = (firstX, firstY)
        if is_inrange(firstX,firstY):
            graph[firstX][firstY] = closestIdx
        else:
            is_live[closestIdx] = False

    graph[rudolf[0]][rudolf[1]] = -1

    for i in range(1, p+1):
        if not is_live[i] or stun[i] >= t:
            continue

        minDist = (pos[i][0] - rudolf[0]) ** 2 + (pos[i][1]-rudolf[1]) ** 2
        moveDir = -1

        for dir in range(4):
            nx = pos[i][0] + dx[dir]
            ny = pos[i][1] + dy[dir]

            if not is_inrange(nx,ny) or graph[nx][ny] > 0:
                continue

            dist = (nx-rudolf[0]) ** 2 + (ny-rudolf[1])**2

            if dist < minDist:
                minDist = dist
                moveDir = dir

        if moveDir != -1:
            nx = pos[i][0] + dx[moveDir]
            ny = pos[i][1] + dy[moveDir]

            # 2.1 산타의 이동으로 인한 충돌
            if nx == rudolf[0] and ny == rudolf[1]:
                stun[i] = t+1

                moveX = -dx[moveDir]
                moveY = -dy[moveDir]

                firstX = nx + moveX * d
                firstY = ny + moveY * d
                lastX, lastY = firstX, firstY

                if d == 1:
                    points[i] += d
                else:
                    # 2.2 산타의 충돌로 인한 상호작용
                    while is_inrange(lastX,lastY) and graph[lastX][lastY]>0:
                        lastX += moveX
                        lastY += moveY

                    # 2.3 연쇄작용이 일어난 가장 마지막 위치에서 시작
                    while lastX != firstX or lastY != firstY:
                        beforeX = lastX - moveX
                        beforeY = lastY - moveY

                        if not is_inrange(beforeX, beforeY):
                            break

                        idx = graph[beforeX][beforeY]

                        if not is_inrange(lastX,lastY):
                            is_live[idx] = False
                        else:
                            graph[lastX][lastY] = graph[beforeX][beforeY]
                            pos[idx] = (lastX,lastY)

                        lastX, lastY = beforeX, beforeY

                    points[i] += d
                    graph[pos[i][0]][pos[i][1]] = 0
                    pos[i] = (firstX, firstY)
                    if is_inrange(firstX, firstY):
                        graph[firstX][firstY] = i
                    else:
                        is_live[i] = False

            else:
                graph[pos[i][0]][pos[i][1]] = 0
                pos[i] = (nx,ny)
                graph[nx][ny] = i
    for i in range(1, p+1):
        if is_live[i]:
            points[i] += 1

for i in range(1,p+1):
    print(points[i], end=' ')














