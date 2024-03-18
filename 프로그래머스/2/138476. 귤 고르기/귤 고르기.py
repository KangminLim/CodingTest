def solution(k, tangerine):
    ans = 0
    tdict = {}
    for tan in tangerine:
        if tan not in tdict:
            tdict[tan] = 1
        else:
            tdict[tan] += 1
    tlst = sorted(tdict.items(), key=lambda x:x[1])
    while k>0:
        k -= tlst.pop()[1]
        ans += 1
    return ans