import heapq
def solution(operations):
    answer = []
    hq = []
    
    for oper in operations:
        x, num = oper.split()
        num = int(num)
        if x == 'I':
            heapq.heappush(hq,num)
        else:
            if hq:
                if num == -1:
                    heapq.heappop(hq)
                else:
                    hq.sort()
                    hq.pop()
            
    hq.sort()
    if hq:
        answer = [hq[-1],hq[0]]
    else:
        answer = [0,0]
        
    return answer