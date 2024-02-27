# Z
def Z(x,y,N):
    global cnt
    if x > r or x+N <=r or y > c or y+N <= c:
        cnt += N**2
        return
    if N > 2:
        N //= 2
        Z(x,y,N)
        Z(x,y+N,N)
        Z(x+N,y,N)
        Z(x+N,y+N,N)
    else:
        if x==r and y==c:
            print(cnt)
        elif x==r and y+1==c:
            print(cnt+1)
        elif x+1==r and y==c:
            print(cnt+2)
        else:
            print(cnt+3)
cnt = 0
N,r,c = map(int,input().split())
Z(0,0,2**N)