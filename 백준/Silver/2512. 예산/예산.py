N = int(input())
lst = list(map(int,input().split()))
M = int(input())

# 1번 조건
if sum(lst) <= M:
    print(max(lst))
# 2번 조건
else:
    start = 1
    end = max(lst)
    result = 0
    lst.sort()
    while start <= end:
        mid = (start+end) // 2
        tmp = 0
        for i in range(N):
            if lst[i] <= mid:
                tmp += lst[i]
            else:
                tmp += mid

        if M-tmp >= 0:
            start = mid + 1
            result = mid
        elif M-tmp < 0:
            end = mid - 1
    print(result)