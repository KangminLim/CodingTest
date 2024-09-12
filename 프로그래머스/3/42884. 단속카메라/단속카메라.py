def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    last_c = -1e9
    for route in routes:
        l_c, r_c = route
        
        if last_c < l_c:
            last_c = r_c
            answer += 1
        
    return answer