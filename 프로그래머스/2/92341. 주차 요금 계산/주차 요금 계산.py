from math import ceil
def solution(fees, records):
    answer = []
    pdict = {}
    tdict = {}
    
    for record in records:
        t,n,c = record.split()
        t = int(t[:2]) * 60 + int(t[3:])
        if c == 'IN':
            pdict[n] = t 
        elif c == 'OUT':
            if n in tdict:
                tdict[n] += (t-pdict[n])
            else:
                tdict[n] = t-pdict[n]
            pdict.pop(n)
            
    for n, t in pdict.items():
        if n in tdict:
            tdict[n] += 1439 - t
        else:
            tdict[n] = 1439 - t
        
    for n, t in sorted(tdict.items(), key=lambda x:x[0]):
        answer.append(fees[1]+max(0,ceil((t-fees[0])/fees[2]))*fees[3])
    
    return answer
