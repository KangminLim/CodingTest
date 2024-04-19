N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    cnt = 0
    v[x] = True

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not v[next_node]:
                v[next_node] = True
                q.append(next_node)
                cnt += 1

    return cnt

v = [False] * (N+1)

print(bfs(1))