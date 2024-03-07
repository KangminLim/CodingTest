from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        time = 0
        x = q.popleft()
        for price in q:
            time += 1
            if x > price:
                break
        answer.append(time)
    
    
    return answer