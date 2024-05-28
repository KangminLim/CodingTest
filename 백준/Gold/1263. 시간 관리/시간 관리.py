# 시간 관리
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort(key=lambda x:x[1], reverse=True)

ans = lst[0][1] - lst[0][0]

for ti,si in lst[1:]:
    if ans > si:
        ans = si-ti
    else:
        ans -= ti

if ans >=0:
    print(ans)
else:
    print(-1)