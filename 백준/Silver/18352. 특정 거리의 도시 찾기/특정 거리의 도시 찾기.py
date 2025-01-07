import sys
input = sys.stdin.readline

N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

v = [-1] * (N+1)

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 0
    while q:
        cur = q.popleft()

        for i in graph[cur]:
            if v[i] == -1:
                v[i] = v[cur] + 1
                q.append(i)

bfs(X)
alst = []

for i in range(1,N+1):
    if v[i] == K:
        alst.append(i)

if not alst: print(-1)
else:
    for ans in alst:
        print(ans)