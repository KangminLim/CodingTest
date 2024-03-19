def solution(dirs):
    # 상하우좌
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    x,y = 0,0
    answer = 0
    visited = [[False] * 5 for _ in range(5)]
    vis = set()
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            dr = 0
        elif dirs[i] == 'D':
            dr = 1
        elif dirs[i] == 'R':
            dr = 2
        elif dirs[i] == 'L':
            dr = 3
        nx = x + dx[dr]
        ny = y + dy[dr]
        if -5<=nx<=5 and -5<=ny<=5:
            vis.add((x,y,nx,ny))
            vis.add((nx,ny,x,y))
            x = nx
            y = ny
                
    return len(vis)//2