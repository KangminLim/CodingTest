# index가 곧 점수다
T =int(input())

for _ in range(T):
    tc = int(input())
    many_cnt = 0
    lst = list(map(int,input().split()))
    cnt = [0] * 101
    for i in lst:
        cnt[i] += 1
    m = max(cnt)
    print("#{} {}".format(tc,max([i for i,v in enumerate(cnt) if v==m])))
