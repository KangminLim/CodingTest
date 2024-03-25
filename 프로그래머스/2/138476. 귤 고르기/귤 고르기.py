def solution(k, tangerine):
    answer = 0
    t_dict = {}
    for tan in tangerine:
        if tan not in t_dict:
            t_dict[tan] = 1
        else:
            t_dict[tan] += 1
    tlst = sorted(t_dict.items(),key = lambda x:x[1])
    while k>0:
        now = tlst.pop()[1]
        k -= now
        answer += 1
    return answer