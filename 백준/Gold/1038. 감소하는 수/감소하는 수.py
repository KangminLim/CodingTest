from itertools import combinations
N = int(input())

ans = []
for i in range(1,11):
    for combination in combinations(range(10),i):
        num = int(''.join([str(s) for s in sorted(combination,reverse=True)]))
        ans.append(num)

ans.sort()

if N < len(ans):
    print(ans[N])
else:
    print(-1)