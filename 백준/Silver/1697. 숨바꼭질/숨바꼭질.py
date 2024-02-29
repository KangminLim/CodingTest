#숨바꼭질
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            break
        for nx in (x-1,x+1,2*x):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10**5
N, K = map(int,input().split())
dist = [0] * (MAX+1)

bfs(N)