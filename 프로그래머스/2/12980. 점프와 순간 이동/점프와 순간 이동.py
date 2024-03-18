def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%2 == 0:
            n //=2
        else: 
            n -= 1
            answer += 1
        if n == 0:
            break
    return answer