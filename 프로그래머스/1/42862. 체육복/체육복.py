def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # lost, reserve 겹친 애 뺴기
    r_lost = set(lost) - set(reserve)
    r_reserve = set(reserve) - set(lost)
    for i in r_reserve:
        if i-1 in r_lost:
            r_lost.remove(i-1)
        elif i+1 in r_lost:
            r_lost.remove(i+1)
        
    return n-len(r_lost)
    