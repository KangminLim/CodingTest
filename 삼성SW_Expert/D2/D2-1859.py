T = int(input())

for tc in range(1,T+1):
    N = int(input())
    N_list = list(map(int,input().split()))
    ans = 0
    max_val = N_list[-1]
    for i in range(N-2,-1,-1):
        if max_val > N_list[i]:
            ans += max_val - N_list[i]
        else :
            max_val = N_list[i]
    print('#{} {}'.format(tc,ans))