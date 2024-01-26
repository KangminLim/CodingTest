import sys
sys.setrecursionlimit(100)
input = sys.stdin.readline
T = int(input())
def fibonnaci(n):
    global z_cnt, o_cnt
    if n==0:
        z_cnt += 1
        return z_cnt
    elif n==1:
        o_cnt += 1
        return o_cnt
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

for tc in range(T):
    N = int(input())
    z_cnt, o_cnt = 0, 0
    fibonnaci(N)
    print(z_cnt, o_cnt)
