def solution(n, m, section):
    answer = 0
    p = [1] * (n+1)
    for s in section:
        p[s] = 0
    
    for s in section:
        if p[s] == 1: continue
        else:
            answer += 1
            for i in range(s,s+m):  
                if i == n+1: break
                if p[i] == 0:
                    p[i] = 1
    return answer        
    