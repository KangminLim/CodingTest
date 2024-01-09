# 최소비용 구하기
import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
M = int(input())
myList = [[] for _ in range(N+1)]
dist = [sys.maxsize] * (N+1)
visit = [False] * (N+1)

for _ in range(M):
    S, E, W = map(int, input().split())
    myList[S].append((E,W))

S_idx, E_idx = map(int,input().split())

def dijkstra(start,end):
    pq = PriorityQueue()
    pq.put((0,start))
    # 우선순위에 데이터를 최단 거리, 노드 순으로 삽입
    dist[start] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visit[now]:
            visit[now] = True
            for n in myList[now]:
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] = dist[now] + n[1]
                    pq.put((dist[n[0]],n[0]))
    return dist[end]

print(dijkstra(S_idx, E_idx))