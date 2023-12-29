N = int(input())
K = int(input())
start = 1
end = K 
ans = 0 

while start <= end:
    mid =int((start+end)/2)
    cnt = 0
    # 중앙값보다 작은 수 계산
    for i in range(1, N+1):
        cnt += min(int(mid/i),N)
    if cnt < K:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)
    