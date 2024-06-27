N = int(input())
lst = [int(input()) for _ in range(N)]
sm = [0] *(2*N+1)

# 거리 리스트 * 2 -> 원으로 된 것을 한 줄로 펴준 것
for i in range(2*N):
    sm[i+1] = sm[i] + lst[i%N]

ans = 0
total, r = sum(lst), 1

for l in range(2*N):
    # r이 범위를 넘어가는지 혹은 부분 배열의 합이 전체 합의 절반인지 확인
    while r < 2*N+1 and sm[r] - sm[l] <= total - (sm[r] - sm[l]):
        ans = max(ans,sm[r]-sm[l])
        r += 1

print(ans)