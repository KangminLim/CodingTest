import sys
input = sys.stdin.readline
N, M = map(int,input().split())
lst = list(map(int,input().split()))
s, e = 0, max(lst)

while s<=e:
    tmp = 0
    mid = (s+e) // 2
    for i in lst:
        if mid < i:
            tmp += (i-mid)
    if tmp >= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)
