def solution(wallpaper):
    x = len(wallpaper)
    y = len(wallpaper[0])
    lux, luy = int(1e9),int(1e9)
    rdx, rdy = -int(1e9), -int(1e9)
    
    for i in range(x):
        for j in range(y):
            if wallpaper[i][j] == '#':
                lux = min(lux,i)
                luy = min(luy,j)
                rdx = max(rdx,i)
                rdy = max(rdy,j)
                
    return [lux,luy,rdx+1,rdy+1]