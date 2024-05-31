# 강의실
import heapq
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort(key=lambda x:(x[1],x[2]))
pq = []
heapq.heappush(pq,lst[0][2]) # 맨처음 종료 시간 넣기

for i in range(1,N):
    if lst[i][1] >= pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq,lst[i][2])

print(len(pq)) # pq가 강의실 개수