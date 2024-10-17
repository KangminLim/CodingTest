import heapq

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort(key=lambda x:(x[0],x[1]))

pq = []
heapq.heappush(pq,lst[0][1])

for i in range(1,N):
    if lst[i][0] >= pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq,lst[i][1])
print(len(pq))