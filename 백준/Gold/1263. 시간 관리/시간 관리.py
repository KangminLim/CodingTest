# 시간 관리
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort(key=lambda x:x[1], reverse = True)

ans = lst[0][1] - lst[0][0]
for i in range(1,N):
    if ans < lst[i][1]:
        ans -= lst[i][0]
    else:
        ans = lst[i][1] - lst[i][0]

if ans >= 0:
    print(ans)
else:
    print(-1)
