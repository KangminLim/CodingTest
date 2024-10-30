N, M = map(int,input().split())

def bt(lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(1,N+1):
        if len(lst) == 0 or max(lst) <= i:
            bt(lst+[i])

bt([])