#효율적으로 해킹하기
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
A = [[] for _ in range(N+1)]
answer = [0] * (N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited = [False] * (N + 1)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)

for _ in range(M):
    S, E = map(int,input().split())
    A[S].append(E)

for i in range(1,N+1):
    BFS(i)

max_val = 0
for i in range(1,N+1):
    max_val = max(max_val, answer[i])

for i in range(1,N+1):
    if max_val == answer[i]:
        print(i, end=' ')