# 특정거리도시찾기
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int,input().split()) # 노드의 수, 에지의 수, 목표 거리, 시작점
A = [[] for _ in range(N+1)]
ans = []
visited = [-1] *(N+1)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)

for _ in range(M):
    S, E = map(int,input().split())
    A[S].append(E)

BFS(X)

for i in range(N+1):
    if visited[i] == K:
        ans.append(i)

if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)