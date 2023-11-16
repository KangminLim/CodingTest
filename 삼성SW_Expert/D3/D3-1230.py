for _ in range(1,11):
    N = int(input())
    O_S = list(map(int,input().split()))
    C_N = int(input())
    C = list(input().split())
    cmd = ''
    pos = -1
    cnt = -1
    for i in range(len(C)):
        if C[i] in ['I','D','A']:
            cmd = C[i]
            pos = -1
            cnt = -1
        else:
            if cmd == 'I':
                if pos == -1:
                    pos = int(C[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(C[i])
                        continue

                    O_S.insert(pos,int(C[i]))
                    pos += 1

            elif cmd == 'D':
                if pos == -1:
                    pos =int(C[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(C[i])
                        for j in range(cnt):
                            del O_S[pos]

            elif cmd == 'A':
                if cnt == -1:
                    cnt = int(C[i])
                else:
                    O_S.append(int(C[i]))
    print('#{}'.format(_),end=' ')
    print(*O_S[:10])