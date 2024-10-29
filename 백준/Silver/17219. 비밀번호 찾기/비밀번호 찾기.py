import sys
input = sys.stdin.readline
N, M = map(int,input().split())
tdict = {}

for _ in range(N):
    k,v = map(str,input().split())
    tdict[k] = v

for _ in range(M):
    k = str(input().rstrip())
    print(tdict[k])

