#효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
A = [[] for _ in range(N+1)]
ans = [0] * (N+1)

def BFS(v):
    queue=deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                ans[i] += 1
                queue.append(i)

for _ in range(M):
    S, E = map(int,input().split())
    A[S].append(E)

for i in range(1, N+1):
    visited = [False] * (N+1)
    BFS(i)

maxVal = 0
for i in range(1, N+1):
    maxVal = max(maxVal,ans[i])

for i in range(1, N+1):
    if maxVal == ans[i]:
        print(i, end=' ')
