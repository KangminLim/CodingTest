N, M = map(int,input().split())
lst = list(map(int,input().split()))

result = 0

start, end = 1, max(lst)

while start <= end:
    cnt = 0
    mid = (start+end) // 2
    for length in lst:
        cnt += length // mid

    if cnt >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)