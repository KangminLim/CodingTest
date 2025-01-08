# 게임
import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 501 for _ in range(501)]

for _ in range(N):
    x1, y1 , x2, y2 = map(int,input().split())
    a1 = min(x1,x2)
    a2 = max(x1,x2)
    b1 = min(y1,y2)
    b2 = max(y1,y2)
    for i in range(a1,a2+1):
        for j in range(b1,b2+1):
            arr[i][j] = 1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    a1 = min(x1, x2)
    a2 = max(x1, x2)
    b1 = min(y1, y2)
    b2 = max(y1, y2)

    for i in range(a1, a2+1):
        for j in range(b1, b2+1):
            arr[i][j] = 2

from collections import deque
def bfs(si,sj):
    q = deque()
    q.append((si,sj,0))
    v = [[False] * 501 for _ in range(501)]
    v[si][sj] = True
    while q:
        ci,cj,cnt = q.popleft()
        if (ci,cj) == (500,500):
            return cnt
        for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if 0<=ni<=500 and 0<=nj<=500 and not v[ni][nj] and arr[ni][nj] != 2:
                if arr[ni][nj] == 1:
                    q.append((ni,nj,cnt+1))
                elif arr[ni][nj] == 0:
                    q.appendleft((ni, nj, cnt))
                v[ni][nj] = True

    return -1

print(bfs(0,0))
