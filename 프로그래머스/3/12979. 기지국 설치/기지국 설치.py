def solution(n, stations, w):
    answer = 0
    need = []
    if stations[0]-w-1 > 0:
        need.append(stations[0]-w-1)
    if (n-stations[-1] - w) > 0:
        need.append(n-stations[-1]-w)
    
    for i in range(len(stations)-1):
        div = stations[i+1]-stations[i] - 1
        div -= (2*w)
        if div > 0:
            need.append(div)
    
    for i in need:
        answer += i // (w*2+1)
        if i%(w*2+1) != 0:
            answer += 1
    
    return answer