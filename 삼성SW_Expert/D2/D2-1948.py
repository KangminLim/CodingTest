T = int(input())
day=[31,28,31,30,31,30,31,31,30,31,30,31]
for tc in range(1,T+1):
    m1, d1, m2, d2 = map(int,input().split())
    answer = 0
    subtraction=0
    month_subtraction=0
    month_ = m2-m1-1
    # print(month_)
    if m1 == m2:
        answer = d2 - d1 + 1
        print('#{} {}'.format(tc, answer))

    elif m1 != m2:
        # if d1 > d2:
        subtraction = (day[m1-1]-d1) + (d2)
        # print(subtraction)
        for i in range(month_):
            month_subtraction += day[m1+i]
        answer = month_subtraction + subtraction + 1
        print('#{} {}'.format(tc,answer))


