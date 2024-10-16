from collections import Counter
def solution(want, number, discount):
    answer = 0
    wdict = {}
    for i in range(len(want)):
        wdict[want[i]] = number[i]
    i = 0
    while i <= len(discount) - 10:
        tdict = Counter(discount[i:i+10])
        if tdict == wdict:
            answer +=1
        i += 1
    
    return answer 