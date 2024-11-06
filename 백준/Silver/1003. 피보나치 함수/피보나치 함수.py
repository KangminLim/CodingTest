N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        print(1,0)
    elif num == 1:
        print(0,1)
    else:
        zcnt = ocnt = 1
        for i in range(2,num):
            zcnt,ocnt = ocnt, zcnt+ocnt
        print(zcnt,ocnt)
