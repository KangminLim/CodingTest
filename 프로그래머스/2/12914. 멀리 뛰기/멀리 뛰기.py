def solution(n):
    
    if n == 1:
        return 1
    
    a = 1 
    b = 2
    
    for i in range(2,n):
        a, b = b, a+b
        
    return b % 1234567