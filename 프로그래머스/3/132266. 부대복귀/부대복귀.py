from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    v = [-1] * (n+1)
    graph =[[] for _ in range(n+1)]
    
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    q.append(destination)
    v[destination] += 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if v[i] == -1:
                q.append(i)
                v[i] = v[cur] + 1
    for i in sources:
        answer.append(v[i])
    return answer