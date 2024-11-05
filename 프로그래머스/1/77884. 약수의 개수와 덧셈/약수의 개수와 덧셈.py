def solution(left, right):
    answer = []
    for i in range(left,right+1):
        tmp = 0
        for j in range(1,i+1):
            if i%j == 0:
                tmp += 1
        answer.append((tmp,i))
    ans = 0 
    for i in range(len(answer)):
        if answer[i][0] % 2 == 0:
            ans += answer[i][1]
        else:
            ans -= answer[i][1]
    
    return ans