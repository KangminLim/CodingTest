from collections import Counter
def solution(k, tangerine):
    answer = 0
    tdict = Counter(tangerine)
    tlst = sorted(tdict.items(), key = lambda x:x[1])
    
    while k > 0:
        k -= tlst.pop()[1]
        answer += 1
    return answer