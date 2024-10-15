import math
def solution(n, words):
    answer = []
    wdict = {}
    last = ''
    for idx, val in enumerate(words):
        if idx ==0 or last[-1] == val[0]:
            print(last,val)
            if val not in wdict:
                wdict[val] = 1
            else:
                if (idx+1)%n == 0:
                    return [n,math.ceil((idx+1)/n)]
                else:
                    return [(idx+1)%n,math.ceil((idx+1)/n)]
        else:
            if (idx+1)%n == 0:
                return [n,math.ceil((idx+1)/n)]
            else:
                return [(idx+1)%n,math.ceil((idx+1)/n)]
        
        last = val
    return [0,0]
