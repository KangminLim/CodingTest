import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
white, blue = 0, 0

def make(a,b,n):
    global white, blue
    color = arr[a][b]
    for i in range(a,a+n):
        for j in range(b,b+n):
            if color != arr[i][j]:
                make(a,b,n//2)
                make(a+n//2, b, n // 2)
                make(a, b+n//2, n // 2)
                make(a+n//2, b+n//2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

make(0,0,N)
print(white)
print(blue)