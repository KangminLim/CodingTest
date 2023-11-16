T = int(input())

for tc in range(1,T+1):
    P,Q,R,S,W = map(int,input().split())
    A, B=0,0
    A = P * W
    if W <=R:
        B=Q
    elif W>R:
        B=Q+(W-R)*S

    if A <=B:
        print('#{} {}'.format(tc,A))
    else:
        print('#{} {}'.format(tc, B))