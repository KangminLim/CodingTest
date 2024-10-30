import heapq, sys
input = sys.stdin.readline
pq = []
N = int(input())
for _ in range(N):
    X = int(input())
    if X == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq,X)
