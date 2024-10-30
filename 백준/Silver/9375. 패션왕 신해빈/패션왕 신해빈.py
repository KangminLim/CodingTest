T = int(input())
for _ in range(T):
    fdict = {}
    N = int(input())
    ans = 1
    for _ in range(N):
        v,k = map(str,input().split())
        if k not in fdict:
            fdict[k] = 1
        else:
            fdict[k] += 1
    for k,v in fdict.items():
        ans *= (v+1)
    ans -= 1
    print(ans)