import heapq
def solution(operations):
    answer = []
    pq = []
    heapq.heapify(pq)
    
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heapq.heappush(pq,num)
        else:
            if pq:
                if num == -1:
                    heapq.heappop(pq)
                # max 힙 구현   
                else:
                    pq.sort()
                    pq.pop()
    pq.sort()
    if not pq:
        return [0,0]
    else:
        return [pq[-1], pq[0]]
