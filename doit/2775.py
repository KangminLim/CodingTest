# 부녀회장이 될거야
import sys
input = sys.stdin.readline
D = [[0 for j in range(15)] for i in range(15)]

for i in range(1,15):
    D[i][1] = 1
    D[0][i] = i

for i in range(1,15):
    for j in range(2,15):
        D[i][j] = D[i][j-1] + D[i-1][j] # 점화식

T = int(input())

for i in range(0,T):
    K = int(input())
    N = int(input())
    print(D[K][N])