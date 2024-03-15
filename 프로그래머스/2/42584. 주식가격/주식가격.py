from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        time = 0
        x = prices.popleft()
        for price in prices:
            time += 1
            if x > price:
                break
        answer.append(time)
        
    return answer