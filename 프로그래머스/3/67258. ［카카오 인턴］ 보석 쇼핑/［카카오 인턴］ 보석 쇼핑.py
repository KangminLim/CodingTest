def solution(gems):
    size = len(gems)
    gdict = {gems[0] : 1}
    answer = [0,size]
    gsize = len(set(gems))
    left, right = 0, 0
    while left < size and right < size:
        
        if len(gdict) == gsize:
            
            if right - left  < answer[1] - answer[0]: 
                answer = [left,right]
            
            else:
                gdict[gems[left]] -= 1
                if gdict[gems[left]] == 0: 
                    del gdict[gems[left]]
                left += 1 
        
        else:
            right += 1
            
            if right == size:
                break
            
            if gems[right] not in gdict:
                gdict[gems[right]] = 1 
            else:
                gdict[gems[right]] += 1
    
    return [answer[0]+1,answer[1]+1]
            
            
            
            
    
        
                    