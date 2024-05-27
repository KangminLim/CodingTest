from collections import deque

N, M = map(int,input().split())

def bfs(start,find):
    q = deque()
    q.append((start,0)) # 시작노드와 거리
    v = [False] * (N+1)
    v[start] = True

    while q:
        cur_node, dist = q.popleft()

        if cur_node == find:
            return dist

        for node, d in graph[cur_node]:
            if not v[node]:
                v[node] = True
                q.append((node,d+dist))


graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,dist = map(int,input().split())
    graph[a].append((b,dist))
    graph[b].append((a,dist))

for _ in range(M):
    a,b = map(int,input().split())
    print(bfs(a,b))
