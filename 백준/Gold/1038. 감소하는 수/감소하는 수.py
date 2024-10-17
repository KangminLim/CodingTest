from itertools import combinations
N = int(input())
answer = []
for i in range(1,11):
    for comb in combinations(range(10),i):
        tmp = int(''.join([str(s) for s in sorted(comb,reverse=True)]))
        answer.append(tmp)
# print(answer)
answer.sort()

if N < len(answer):
    print(answer[N])
else:
    print(-1)