def solution(s):
    s = list(map(str,s.split(' ')))
    answer = []
    
    for i in range(len(s)):
        tmp = ''
        for j in range(len(s[i])):
            if j==0:
                tmp += s[i][j].upper()
            else:
                tmp += s[i][j].lower()
        answer.append(tmp)
    
        
    
    return ' '.join(answer)