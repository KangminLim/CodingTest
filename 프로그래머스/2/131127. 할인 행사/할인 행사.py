from collections import Counter
def solution(want, number, discount):
    answer = 0
    wdict = {}
    
    for i in range(len(want)):
        wdict[want[i]] = number[i]

    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if wdict == c:
            answer += 1
            
    return answer