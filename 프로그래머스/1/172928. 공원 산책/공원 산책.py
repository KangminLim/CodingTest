# def simul(dr,dist,park):
#     d = -1
#     if dr == 'N' : d = 0
#     elif dr == 'E' : d = 1
#     elif dr == 'S' : d = 2
#     else: d = 3
    
#     dx,dy = [-1,1,0,0],[0,0,-1,1]
#     for i in range(len(park)):
#         for j in range(len(park[0]):
#             if 
    
    
def solution(park, routes):
    d = -1
    pos = (-1,-1)
    di,dj = [-1,1,0,0],[0,0,-1,1]
    N = len(park)
    M = len(park[0])
    new_park = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_park[i][j] = park[i][j]
    for route in routes:
        dr,dist = route.split()
        if dr == 'N' : d = 0
        elif dr == 'S' : d = 1
        elif dr == 'W' : d = 2
        else: d = 3
        for i in range(N):
            for j in range(M):
                if new_park[i][j] == 'S': 
                    pos = (i,j)
        ci,cj = pos
        flag = 0
        for m in range(1,int(dist)+1):
            ni,nj = ci + di[d]*m, cj+dj[d]*m
            if not (0<=ni<N and 0<=nj<M):
                flag = 1
                break
            elif 0<=ni<N and 0<=nj<M:
                if new_park[ni][nj] == 'X':
                    flag = 1
                    break
        if flag == 0:
            new_park[ci][cj] = 'O'
            new_park[ni][nj] = 'S'
            pos = (ni,nj)
            
    return pos
    