aset = set()
bset = set()
tset = set()
answer = []
N, M = map(int,input().split())
for _ in range(N):
    ch = str(input())
    aset.add(ch)
    tset.add(ch)
for _ in range(M):
    ch = str(input())
    bset.add(ch)
    tset.add(ch)

for t in tset:
    if t in aset and t in bset:
        answer.append(t)
answer.sort()
print(len(answer))
for a in answer:
    print(a)