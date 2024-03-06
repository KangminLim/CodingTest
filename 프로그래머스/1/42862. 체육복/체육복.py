def solution(n, lost, reserve):

    f_reserve = [r for r in reserve if r not in lost]
    f_lost = [l for l in lost if l not in reserve]
    f_reserve.sort()
    for r in f_reserve:
        f = r-1
        b = r+1
        
        if f in f_lost:
            f_lost.remove(f)
        elif b in f_lost:
            f_lost.remove(b)
    
    return n - len(f_lost)