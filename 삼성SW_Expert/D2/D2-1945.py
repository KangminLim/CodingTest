T=int(input())

for tc in range(1,T+1):
    N = int(input())
    print('#{}'.format(tc), end=' ')
    cur_N=N
    a,b,c,d,e=0,0,0,0,0

    for i in range(N):
        if cur_N%2==0:
           cur_N = cur_N//2
           # print(cur_N)
           a +=1
        elif cur_N%3==0:
           cur_N = cur_N//3
           # print(cur_N)
           b +=1
        elif cur_N%5==0:
           cur_N = cur_N//5
           # print(cur_N)
           c +=1
        elif cur_N%7==0:
           cur_N = cur_N//7
           # print(cur_N)
           d +=1
        elif cur_N % 11 == 0:
           cur_N = cur_N // 11
           # print(cur_N)
           e += 1
    print(a,b,c,d,e,end='')
    print()