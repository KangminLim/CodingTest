for _ in range(10):
    O_N = int(input())
    O_S = list(map(str,(input().split())))
    C_N = int(input())
    C = list(map(str,input().split()))
    R_S = []
    type  =''
    pos = -1
    cnt = -1
    for i in range(len(C)):
        if C[i] == 'I':
            type = C[i]
            pos = -1
            cnt = -1
        else:
            if type == 'I':
                if pos == -1:
                    pos = int(C[i])
                    continue
                else :
                    if cnt == -1:
                        cnt = int(C[i])
                        continue
                    O_S.insert(pos,C[i])
                    pos += 1
    print('#%d' % _, end=' ')
    print(*O_S[:10])
