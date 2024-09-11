def solution(n):
    answer = 0
    F = [0] * (n+1)
    F[0], F[1] = 0, 1
    
    for i in range(2,n+1):
        F[i] = F[i-1] + F[i-2]
    
    return F[-1] % 1234567
    