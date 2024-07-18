def solution(msg):
    answer = []
    adict = {}
    for i in range(26):
        adict[chr(i+65)] = i+1
    
    s, e = 0, 0
    while True:
        e += 1
        if e == len(msg):
            answer.append(adict[msg[s:e]])
            break
        if msg[s:e+1] not in adict.keys():
            adict[msg[s:e+1]] = len(adict) + 1
            answer.append(adict[msg[s:e]])
            s = e
    return answer