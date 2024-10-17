def solution(k, dungeons):
    answer = -1
    v = [False] * len(dungeons)
    
    def dfs(sm,cnt):
        nonlocal answer
        if cnt > answer:
            answer = cnt
            
        for i in range(len(dungeons)):
            if sm >= dungeons[i][0] and not v[i]:
                v[i] = True
                dfs(sm-dungeons[i][1],cnt+1)
                v[i] = False
    dfs(k,0)
    
    return answer