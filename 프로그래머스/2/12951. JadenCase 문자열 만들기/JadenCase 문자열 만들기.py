def solution(s):
    s = list(map(str,s.split(' ')))
    alst = []
    for ch in s:
        tmp = ''
        for i in range(len(ch)):
            if i == 0:
                if ch[i].isalpha():
                    tmp += ch[i].upper()
                else:
                    tmp += ch[i]
            else:
                tmp += ch[i].lower()
        alst.append(tmp)
    return ' '.join(alst)