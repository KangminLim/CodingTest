import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int,input().split()))
nlst = sorted(set(lst))

adict = {nlst[i]: i for i in range(len(nlst))}

for i in range(len(lst)):
    print(adict[lst[i]],end=' ')
