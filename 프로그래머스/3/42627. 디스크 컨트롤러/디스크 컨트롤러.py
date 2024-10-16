import heapq
def solution(jobs):
    answer, now, i = 0,0 ,0
    start = -1
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now: 
                heapq.heappush(heap,[j[1],j[0]])
        
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
        else:
            now += 1
    
    return answer//len(jobs)