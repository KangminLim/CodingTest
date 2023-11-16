def re(n,m):
    if m>1:
        return n*re(n,m-1)
    else:
        return n
for tc in range(1,11):
    _ =input()
    N,M = map(int,input().split())
    print(f'#{tc} {re(N,M)}')