import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int,input().split())
K = int(input())
dist = [sys.maxsize]  * (V+1)
visited = [False] * (V+1)
graph = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

q.put((0,K))
dist[K] = 0

while q.qsize() > 0:
    cur = q.get()
    cur_v = cur[1]

    if not visited[cur_v]:
        visited[cur_v] = True
        for tmp in graph[cur_v]:
            next, value = tmp
            if dist[next] > dist[cur_v] + value: # 최소 거리로 업데이트
                dist[next] = dist[cur_v] + value
                # 가중치가 정렬 기준이므로 순서를 가중치, 목표 노드 순으로 우선순위 큐 설정
                q.put((dist[next],next))

for i in range(1,V+1):
    if visited[i]:
        print(dist[i])
    else:
        print('INF')