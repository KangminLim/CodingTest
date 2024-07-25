def solution(n):
    answer = []
    while n:
        tmp = n % 3
        # 3의 배수면 4
        if tmp == 0:
            tmp = 4 
            n -= 1
        answer.append(str(tmp))
        n //= 3
    answer = answer[::-1]
        
    return ''.join(answer)