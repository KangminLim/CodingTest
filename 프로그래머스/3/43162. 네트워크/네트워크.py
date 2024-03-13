def solution(n, computers):
    
    def dfs(v):
        visited[v] = True
        for i in range(n):
            if not visited[i] and computers[v][i]:
                dfs(i)
        return
    
    answer = 0
    visited = [False] * n
    
    for node in range(n):
        if not visited[node]:
            dfs(node)
            answer += 1
    
    return answer