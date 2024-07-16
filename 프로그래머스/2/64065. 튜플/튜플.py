def solution(s):
    answer = []
    slice_s = s[2:-2]
    slice_s = slice_s.split('},{')
    slice_s.sort(key=len)
    for tmp in slice_s:
        tnum = list(map(int,tmp.split(',')))
        for anum in tnum:
            if anum not in answer:
                answer.append(anum)
    return answer