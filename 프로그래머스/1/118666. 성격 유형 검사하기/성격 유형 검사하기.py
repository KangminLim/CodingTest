def solution(survey, choices):
    R, T, F, C, M, J, A, N = 0,0,0,0,0,0,0,0
    cdict = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    for i in range(len(survey)):
        cur_s = survey[i]
        cur_c = choices[i]
        
        if cur_c >=5:
            idx = 1
            if cur_s[idx] == 'R':
                R += cdict[cur_c]
            elif cur_s[idx] == 'T':
                T += cdict[cur_c]
            elif cur_s[idx] == 'F':
                F += cdict[cur_c]   
            elif cur_s[idx] == 'C':
                C += cdict[cur_c]   
            elif cur_s[idx] == 'M':
                M += cdict[cur_c]   
            elif cur_s[idx] == 'J':
                J += cdict[cur_c]   
            elif cur_s[idx] == 'A':
                A += cdict[cur_c]   
            elif cur_s[idx] == 'N':
                N += cdict[cur_c]   
        
        elif cur_c <= 3:
            idx = 0
            if cur_s[idx] == 'R':
                R += cdict[cur_c]
            elif cur_s[idx] == 'T':
                T += cdict[cur_c]
            elif cur_s[idx] == 'F':
                F += cdict[cur_c]   
            elif cur_s[idx] == 'C':
                C += cdict[cur_c]   
            elif cur_s[idx] == 'M':
                M += cdict[cur_c]   
            elif cur_s[idx] == 'J':
                J += cdict[cur_c]   
            elif cur_s[idx] == 'A':
                A += cdict[cur_c]   
            elif cur_s[idx] == 'N':
                N += cdict[cur_c]   
        else:
            continue
    answer = ''

    if R >= T: answer += 'R' 
    else: answer += 'T'
    if C >= F: answer += 'C' 
    else: answer += 'F'
    if J >= M: answer += 'J' 
    else: answer += 'M'
    if A >= N: answer += 'A' 
    else: answer += 'N'
    
    return answer