N,M = map(int,input().split())

def bt(lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1,N+1):
        if not v[i] and (len(lst) == 0 or max(lst) < i):
            v[i] = True
            bt(lst+[i])
            v[i] = False

v = [0] * (N+1)
bt([])
