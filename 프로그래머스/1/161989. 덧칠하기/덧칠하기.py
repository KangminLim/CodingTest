def solution(n, m, section):
    arr = [True] * (n+1)
    arr[0] = False
    cnt = 0
    
    for s in section:
        arr[s] = False
    
    start = 0
    for i in range(1,n+1):
        if not arr[i]:
            start = arr[i]
            arr[i] = True
            cnt += 1
            for j in range(m):
                if i+j > n:
                    break
                arr[i+j] = True        
    return cnt    
    
    