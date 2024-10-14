def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    cur = 30001
    print(routes)
    for route in routes:
        start, end = route
        if cur > end: 
            cur = end 
            answer += 1
        elif cur < start:
            cur = end 
            answer += 1
    return answer