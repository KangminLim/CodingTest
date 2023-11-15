# matrix
INF = 999999999
graph = [[0,7,5],[7,0,INF], [5,INF,0]]
print(graph)

# list
graph = [[] for _ in range(3)]
# node 0에 연결된 노드 정보 저장(노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))
# node 1 
graph[1].append((0,7))
graph[2].append((0,5))

print(graph)