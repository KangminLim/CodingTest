def solution(n):
    answer = 0
    temp = 0
    for i in range(1,n+1):
        temp = i
        for j in range(i+1,n+1):
            temp += j
            if temp > n:
                break
            elif temp == n:
                answer += 1
                break
    # 자기자신
    answer += 1
    return answer