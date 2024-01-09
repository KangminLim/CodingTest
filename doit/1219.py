# 세일즈맨의 고민
import sys
input = sys.stdin.readline
N, sCity, eCity, M = map(int,input().split())
edges = []
distance = [-sys.maxsize] * N

for _ in range(M):
    start, end, price = map(int,input().split())
    edges.append((start, end, price))

cityMoney = list(map(int,input().split()))

# 변형된 벨만-포드 수행
distance[sCity] = cityMoney[sCity]

# 양수 사이클이 전파되도록 충분히 큰 수로 반복
for i in range(N+101):
    for start, end, price in edges:
        if distance[start] == -sys.maxsize: # 출발 노드가 미 방문 노드면 skip
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cityMoney[end] - price:
            distance[end] = distance[start] + cityMoney[end] - price
            if i >= N-1:
                distance[end] = sys.maxsize

if distance[eCity] == -sys.maxsize:
    print("gg")
elif distance[eCity] == sys.maxsize:
    print('Gee')
else:
    print(distance[eCity])