def solution(sizes):
    

    mx = []
    mn = []
    
    for i in range(len(sizes)):
        n_min = min(sizes[i])
        n_max = max(sizes[i])

        mx.append(n_max)
        mn.append(n_min)
        
    return max(mx)*max(mn)
       