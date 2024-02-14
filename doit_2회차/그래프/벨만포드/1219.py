# 세일즈맨의고민
import sys
input = sys.stdin.readline
N, sCity, eCity, M = map(int,input().split())
edges = []
distance = [-sys.maxsize] * N

for _ in range(M):
    s, e, p = map(int,input().split())
    edges.append((s,e,p))

cityMoney = list(map(int,input().split()))

# 변형된 벨만-포드
distance[sCity] = cityMoney[sCity] # 출발 초기화

# 양수 사이클이 저파되도록 충분히 큰 수로 반복
for i in range(N+101):
    for s, e, p in edges:
        if distance[s] == -sys.maxsize:
            continue
        elif distance[s] == sys.maxsize:
            distance[e] = sys.maxsize
        elif distance[e] < distance[s] + cityMoney[e] - p:
            distance[e] = distance[s] + cityMoney[e] - p
            if i >= N-1:
                distance[e] = sys.maxsize

if distance[eCity] == -sys.maxsize:
    print('gg')
elif distance[eCity] == sys.maxsize:
    print('Gee')
else:
    print(distance[eCity])