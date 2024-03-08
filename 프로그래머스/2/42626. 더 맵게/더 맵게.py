import heapq
def solution(scoville, K):
    heapq.heapify(scoville)      
    answer = 0
    
    while len(scoville)>=2 and scoville[0]<K:
        if all(sco >=K for sco in scoville):
            return answer
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new_scoville = first + second * 2
            heapq.heappush(scoville,new_scoville)
            answer += 1
    if len(scoville)<=1 and scoville[0]<K:
        return - 1
    return answer