T = int(input())

for tc in range(1,T+1):
    S=input()
    if S == S[::-1]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))