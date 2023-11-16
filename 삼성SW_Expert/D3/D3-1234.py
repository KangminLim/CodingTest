for TC in range(10):
    N, pw = input().split()
    N = int(N)
    stk = []
    for c in pw:
        if stk and c == stk[-1]:
            stk.pop()
        else:
            stk.append(c)
    result = ''.join(stk)

    print('#{} {}'.format(TC+1, result))