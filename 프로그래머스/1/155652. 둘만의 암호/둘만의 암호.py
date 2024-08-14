def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    
    for ch in s:
        tmp = 0 
        while tmp != index:
            if ch == 'z':
                ch = chr(ord('a'))
            else:
                ch = chr(ord(ch) + 1)
                
            if ch not in skip:
                tmp += 1
        answer += ch
    return answer