def solution(n):
    answer = []
    a = 0
    b = 1
    for i in range(2,n+1):
        a,b = b, a+b
        answer.append(b)
    return answer[-1] %1234567