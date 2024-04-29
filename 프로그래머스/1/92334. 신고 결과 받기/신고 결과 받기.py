def solution(id_list, report, k):
    answer = []
    rdict = {}
    adict = {}
    for i in id_list:
        rdict[i] = 0
        adict[i] = 0
    rset = set()
    for r in report:
        # 유저, 신고한 아이디
        user,i = r.split(' ')
        # 중복 신고 방지 
        if (user,i) in rset: 
            continue
        else:
            # 신고 내역 
            rset.add((user,i))
            rdict[i] += 1
    
    for user,i in rset:
        if rdict[i] >= k:
            adict[user] += 1
    for k in adict:
        answer.append(adict[k])
    return answer