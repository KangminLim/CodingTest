def solution(s):
    s = s.split(' ')
    answer = []    
    for i in s:
        res = ''
        for j in range(len(i)):
            if j==0:  
                res += i[j].upper()
            else:
                res += i[j].lower()
        answer.append(res)
    return ' '.join(answer)