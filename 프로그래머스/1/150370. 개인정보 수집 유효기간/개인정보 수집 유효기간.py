def solution(today, terms, privacies):
    ty,tm,td = today.split('.')
    # 숫자로 변환
    tn = int(ty)*12*28 + int(tm)*28 + int(td)
    tdict = {}
    for term in terms:
        a,b = term.split(' ')
        tdict[a] = b
        
    tmp = []
    
    for privacy in privacies:
        a,b = privacy.split(' ')
        py,pm,pd = a.split('.')
        pn = int(py)*12*28 + int(pm)*28 + int(pd)
        pc = int(tdict[b]) * 28
        pn = pn + pc 
        tmp.append(pn)
        
    answer = []
    for idx, val in enumerate(tmp):
        if val <= tn:
            answer.append(idx+1)
            
    return answer
