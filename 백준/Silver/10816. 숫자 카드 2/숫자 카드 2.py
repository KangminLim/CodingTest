N = int(input())
nlst = list(map(int,input().split()))
M = int(input())
mlst = list(map(int,input().split()))
ndict = {}
for n in nlst:
    if n not in ndict:
        ndict[n] = 1
    else:
        ndict[n] += 1

for m in mlst:
    if m in ndict:
        print(ndict[m], end=' ')
    else:
        print(0,end=' ')