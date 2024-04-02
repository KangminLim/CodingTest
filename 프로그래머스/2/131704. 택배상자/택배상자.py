from collections import deque
def solution(order):
    q = deque()
    order = deque(order)
    answer = []
    for i in range(1,len(order)+1):
        q.append(i)
        while q:
            if q[-1] == order[0]:
                answer.append(q.pop())
                order.popleft()
                
            else: 
                break
    
    return len(answer)