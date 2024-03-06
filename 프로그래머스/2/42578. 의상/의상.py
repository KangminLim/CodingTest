def solution(clothes):
    clo = {}
    for clothe in clothes:
        if clothe[1] not in clo.keys():
            clo[clothe[1]] = 1
        else:
            clo[clothe[1]] += 1
    ans = 1
    for key, value in clo.items():
        ans *= (value+1)
        
    return ans-1