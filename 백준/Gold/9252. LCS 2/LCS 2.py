# LCS 2
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
A = list(input())
B = list(input())
A.pop()
B.pop()

dp = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
path = []

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])

def getText(r,c):
    if r==0 or c==0:
        return

    if A[r-1] == B[c-1]:
        path.append(A[r-1])
        getText(r-1,c-1)
    else:
        if dp[r-1][c] > dp[r][c-1]:
            getText(r-1,c)
        else:
            getText(r,c-1)

getText(len(A),len(B))

# for i in range(len(path)-1,-1,-1):
#     print(path[i])
path = path[::-1]
print(''.join(path))