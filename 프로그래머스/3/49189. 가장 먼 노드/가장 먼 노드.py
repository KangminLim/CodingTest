from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] * n for _ in range(n)]
    for vertex in edge:
        a,b = vertex
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        
    def bfs(start):
        q = deque()
        q.append(start)
        v = [-1] * n
        v[start] = 0
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if v[i] == -1:
                    q.append(i)
                    v[i] = v[cur] + 1 
        return v
    
    distance = bfs(0)

    for d in distance:
        if d == max(distance):
            answer += 1
    
    return answer