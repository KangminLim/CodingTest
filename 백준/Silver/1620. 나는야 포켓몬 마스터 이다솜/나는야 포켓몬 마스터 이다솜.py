# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dic1 = {}
dic2 = {}

for i in range(N):
    name = input().strip()
    dic1[name] = (i+1)
    dic2[i+1] = name

for i in range(M):
    action =input().strip()
    if action.isdigit():
        print(dic2[int(action)])
    else:
        print(dic1[action])