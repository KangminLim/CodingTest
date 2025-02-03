import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M, V = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

ans1 = []
v1 = [False] * (N+1)

def dfs(cur,v,alst):
    alst.append(cur)
    v[cur] = True

    for i in graph[cur]:
        if not v[i]:
            dfs(i,v1,alst)

dfs(V,v1,ans1)
print(*ans1)

from collections import deque
ans2 = []
v2 = [False] * (N+1)

def bfs(start,v,alst):
    q = deque()
    q.append(start)
    v[start] = True
    while q:
        cur = q.popleft()
        alst.append(cur)
        for i in graph[cur]:
            if not v[i]:
                q.append(i)
                v[i] = True
bfs(V,v2,ans2)
print(*ans2)