def solution(survey, choices):
    answer = ''
    N = len(survey)
    s_dict = {}
    c_dict = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    sur = 'RTCFJMAN'
    for i in sur:
        s_dict[i] = 0
        
    for i in range(N):
        sur = survey[i]
        cho = choices[i]
        if 1<=cho<=3:
            s_dict[sur[0]] += c_dict[cho] 
        elif 5<=cho<=7:
            s_dict[sur[1]] += c_dict[cho]
    
    if s_dict['R'] >= s_dict['T']:
        answer += 'R'
    else : answer += 'T'
    
    if s_dict['C'] >= s_dict['F']:
        answer += 'C'
    else : answer += 'F'
    
    if s_dict['J'] >= s_dict['M']:
        answer += 'J'
    else : answer += 'M'
    
    if s_dict['A'] >= s_dict['N']:
        answer += 'A'
    else : answer += 'N'
    
    
    return answer