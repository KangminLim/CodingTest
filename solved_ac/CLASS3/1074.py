# Z
N,r,c = map(int,input().split())
dx = [0,1,0,1]
dy = [0,0,1,1]
mp = [[0] * (2**N) for _ in range(2**N)]
cx, cy = 0, 0
cnt = 0
for i in range(0,2**N,2):
    cx, cy = cx +i, cy+i
    for dr in range(4):
        nx,ny = cx+dx[dr], cy+dy[dr]
        cnt += 1
        print(nx,ny)
        if nx == c and ny == r:
            print(cnt)
            break