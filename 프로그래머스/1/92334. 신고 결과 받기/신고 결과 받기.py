def solution(id_list, report, k):
    # 중복 제거
    report = set(report)
    report = list(report)
    idict = {}
    fdict = {}
    for id in id_list:
        idict[id] = 0
        fdict[id] = []
    for rep in report:
        s, r = rep.split()
        idict[r] += 1
        fdict[s].append(r)
    answer = []
    for id in id_list:
        tmp = 0
        for fk in fdict:
            if idict[fk] >= k and fk in fdict[id]:
                tmp += 1
        answer.append(tmp)
                    
    
    return answer