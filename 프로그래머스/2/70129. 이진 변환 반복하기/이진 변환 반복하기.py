def solution(s):
    answer = []
    ccnt = 0
    zcnt = 0
    while True:
        tmp = ''
        ccnt += 1
        for i in s:
            if i == '1':
                tmp += i
            else:
                zcnt += 1
        s = bin(len(tmp))[2:]
        if s == '1':
            break
    return [ccnt,zcnt]