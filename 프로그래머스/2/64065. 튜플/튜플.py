def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=lambda x:len(x))
    for i in s:
        i = i.split(',')
        for ch in i:
            if int(ch) not in answer:
                answer.append(int(ch))
        
    return answer