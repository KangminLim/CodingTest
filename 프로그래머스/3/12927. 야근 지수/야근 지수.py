# 최대 힙 
import heapq
def solution(n, works):
    answer = 0
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        work = heapq.heappop(works)
        work += 1 
        heapq.heappush(works,work)
    
    return sum(x**2 for x in works if x < 0)