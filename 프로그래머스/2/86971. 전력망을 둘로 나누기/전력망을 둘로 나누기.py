from collections import deque

def solution(n, wires):
    result = n
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(x):
        visited = [False] * (n+1)
        q = deque()
        q.append(x)
        visited[x] = True
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    cnt += 1
        return cnt
        
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        
        result = min(abs(bfs(a)-bfs(b)),result)
        
        graph[a].append(b)
        graph[b].append(a)
    
    return result