N = int(input())
lst = list(map(int,input().split()))
B, C =map(int,input().split())

ans = N # 총감독관은 시험장의 개수만큼
for n in lst:
    if n-B>0: #부감독관
        ans += (n-B+C-1)//C
print(ans)
