import heapq
def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        cur = heapq.heappop(works)
        cur += 1
        heapq.heappush(works,cur)
    ans = 0
    for work in works:
        ans += work**2
    return ans