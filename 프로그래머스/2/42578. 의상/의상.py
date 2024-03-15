def solution(clothes):
    clo = {}
    for clothe in clothes:
        if clothe[1] not in clo:
            clo[clothe[1]] = 1
        else:
            clo[clothe[1]] += 1
            
    answer = 1
    for idx, val in clo.items():
        answer *= (val+1) 
    
    return answer-1