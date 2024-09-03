def solution(park, routes):
    N = len(park)
    M = len(park[0])
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                si,sj = i,j
    ddict = {'N' : 0,
            'S': 1,
            'W': 2,
            'E': 3}
    di,dj = [-1,1,0,0],[0,0,-1,1]
    
    
    for route in routes:
        dr, mul = route.split()
        flag = True
        ti,tj = si,sj
        for m in range(1,int(mul)+1):
            ni, nj = ti + di[ddict[dr]], tj + dj[ddict[dr]]
            if 0<=ni<N and 0<=nj<M and park[ni][nj] != 'X':
                ti,tj = ni,nj
            else:
                flag = False
                break
        if flag:
            si,sj = ti,tj

    return [si,sj]