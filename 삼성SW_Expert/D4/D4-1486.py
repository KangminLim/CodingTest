T = int(input())

def dfs(n,sm):
    global ans
    if ans <= sm-B:
        return

    if n==N:
        if sm>= B:
            ans = min(ans,sm-B)
        return
    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)

for tc in range(1,T+1):
    N, B = map(int,input().split())
    lst = list(map(int, input().split()))

    ans = N * 10000
    dfs(0,0)
    print(f'#{tc} {ans}')