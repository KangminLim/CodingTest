def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(0,len(t)-l+1):
        temp = t[i:i+l]
        if int(temp) <= int(p):
            answer += 1
    return answer