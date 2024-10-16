from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for road in roads:
        a,b = road
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    def bfs(start):
        q = deque()
        q.append(start)
        v = [-1] * (n+1)
        v[start] = 0
        while q:
            cur = q.popleft()
            
            # if cur == destination:
            #     return v[cur]
            for i in graph[cur]:
                # print(v)
                # print(i,graph[i]) 
                if v[i] == -1:
                    # print(i)
                    q.append(i)
                    v[i] = v[cur] + 1  
        
        return v
    
    v = bfs(destination)
    for source in sources:
        answer.append(v[source])

    
    return answer