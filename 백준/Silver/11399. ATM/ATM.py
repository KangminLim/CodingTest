N = int(input())
lst = list(map(int,input().split()))
lst.sort()
tmp = ans = 0
for i in range(N):
    tmp += lst[i]
    ans += tmp
print(ans)