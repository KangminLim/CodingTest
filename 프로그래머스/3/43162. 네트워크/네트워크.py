def solution(n, computers):        
    answer = 0
    v = [False] * n
    
    def dfs(cur):
        v[cur] = True
        for i in range(n):
            if not v[i] and computers[cur][i]: 
                dfs(i)
        return
    
    for i in range(n):
        if not v[i]:
            dfs(i)
            answer += 1
    return answer