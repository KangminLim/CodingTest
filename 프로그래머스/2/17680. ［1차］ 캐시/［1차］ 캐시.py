from collections import deque
def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            q.append(city)
            if len(q) > cacheSize:
                q.popleft()
    return answer