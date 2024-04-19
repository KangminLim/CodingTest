from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(x):
        q = deque()
        q.append(x)
        v = [False] * (n+1)
        v[x] = True
        cnt= 1
        while q: 
            cur = q.popleft()
            for node in graph[cur]:
                if not v[node]:
                    q.append(node)
                    v[node] = True
                    cnt += 1
        return cnt
    
    result = n
    
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        result = min(abs(bfs(a)-bfs(b)), result)
        
        graph[a].append(b)
        graph[b].append(a)

    return result