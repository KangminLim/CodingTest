N = int(input())
nlst = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
mn = int(1e9)
mx = -int(1e9)
def bt(i,sm):
    global mn,mx,add,sub,mul,div
    if i == N:
        mn = min(mn,sm)
        mx = max(mx,sm)
    else:
        if add > 0:
            add -= 1
            bt(i+1,sm + nlst[i])
            add += 1
        if sub > 0:
            sub -= 1
            bt(i+1,sm - nlst[i])
            sub += 1
        if mul > 0:
            mul -= 1
            bt(i+1,sm * nlst[i])
            mul += 1
        if div > 0:
            div -= 1
            bt(i+1, int(sm / nlst[i]))
            div += 1
bt(1,nlst[0])

print(int(mx))
print(int(mn))