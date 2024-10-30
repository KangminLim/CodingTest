N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
v = [False] * len(lst)
def bt(tlst):
    if len(tlst) == M:
        print(*tlst)
        return

    for i in range(len(lst)):
        if not v[i]:
            v[i] = True
            bt(tlst+[lst[i]])
            v[i] = False

bt([])