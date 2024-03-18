def solution(s):
    s= s.split(' ')
    s.sort()
    mx = -int(1e9)
    mn = int(1e9)
    
    for i in s:
        if mx < int(i):
            mx = int(i)
        if mn > int(i):
            mn = int(i)
    return ''.join(str(mn)) + ' ' + ''.join(str(mx)) 
    