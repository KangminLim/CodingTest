def solution(n):
    answer = []
    a = 1 # F(1)
    b = 1 # F(2)
    for i in range(n-2):
        a,b = b, a+b
        answer.append(b)
    return answer[-1] % 1234567