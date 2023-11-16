for tc in range(1,11):
    n = int(input())
    data = list(map(int,input().split()))
    o = int(input())
    order = list(input().split())

    type=''
    pos = -1
    cnt = -1
    for i in range(len(order)):
        if order[i] in ['I', 'D']:
            type = order[i]
            pos=-1
            cnt=-1
        else:
            if type == 'I' :
                if pos == -1:
                    pos =int(order[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(order[i])
                        continue
                    data.insert(pos, order[i])
                    pos +=1

            elif type == 'D':
                if pos == -1:
                    pos = int(order[i])
                    continue
                else:
                    if cnt == -1:
                        cnt = int(order[i])
                        for j in range(cnt):
                            del data[pos]
    print('#{}'.format(tc),end=' ')
    print(*data[:10])