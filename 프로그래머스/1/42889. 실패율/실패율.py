def solution(N, stages):
    answer = []
    stages_s = []
    l = len(stages)
    tmp_l = l
    # 현재 스테이지 번호
    for i in range(1,N+1):
        tmp = stages.count(i) 
        if tmp_l == 0:
            stages_s.append((0,i))
        else:
            stages_s.append((tmp/tmp_l,i))
        tmp_l -= tmp
    stages_s.sort(key=lambda x:(-x[0],x[1]))
    answer = [x[1] for x in stages_s]
    return answer