def solution(n, s):
    answer = []
    d,m = divmod(s,n)
    if d == 0:
        return [-1]
    
    for _ in range(n-m):
        answer.append(d)
    
    for _ in range(m):
        answer.append(d+1)
    
    
    return answer