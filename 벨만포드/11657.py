# 타임머신
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
edges = []
distance = [sys.maxsize] * (N+1)
for i in range(M): # 에지 데이터 저장
    S, E, T = map(int,input().split())
    edges.append((S, E, T))

# 벨만 포드 수행
distance[1] = 0
for _ in range(N-1):
    for S,E,T in edges:
        if distance[S] != sys.maxsize and distance[E] > distance[S] + T :
            distance[E] = distance[S] + T

# 음수 사이클 확인
mCycle = False

for S, E, T in edges:
    if distance[S] != sys.maxsize and distance[E] > distance[S] + T:
        mCycle = True

if not mCycle:
    for i in range(2,N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)

else:
    print(-1)
