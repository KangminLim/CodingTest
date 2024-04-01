import heapq
def solution(operations):
    answer = []
    hq = []
    
    for operation in operations:
        alphabet, number = operation.split()
        number = int(number)
        
        if alphabet == 'I':
            heapq.heappush(hq,number)
            
        else: 
            if hq:
                if number == -1:
                    heapq.heappop(hq) # 최솟값을삭제
                else:
                    hq.sort()
                    hq.pop()
                    
    hq.sort()
    if hq: 
        answer = [hq[-1],hq[0]]
    else:
        answer = [0,0]
    
    return answer