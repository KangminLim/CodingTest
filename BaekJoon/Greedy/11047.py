N,K = map(int,input().split())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
cnt = 0

for i in range(len(lst)):
    if lst[i] > K:
        continue
    elif lst[i] <= K:
        cnt += (K//lst[i])
        K -= (K//lst[i]) * lst[i]
        
print(cnt)