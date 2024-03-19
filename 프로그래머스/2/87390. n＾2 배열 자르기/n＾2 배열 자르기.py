def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        div,mod = divmod(i,n)
        answer.append(max(div,mod)+1)        
        
    return answer