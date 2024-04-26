def solution(topping):
    tdict = {}
    for t in topping:
        if t not in tdict:
            tdict[t] = 1
        else:
            tdict[t] += 1
    
    adict = {}    
    answer = 0
    for i in topping:
        tdict[i] -= 1
        if i not in adict:
            adict[i] = 1
        else: 
            adict[i] += 1
            
        if tdict[i] == 0:
            tdict.pop(i)
        
        if len(tdict) == len(adict):
            answer += 1 
    return answer
