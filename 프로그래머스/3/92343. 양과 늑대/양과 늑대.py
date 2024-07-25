def solution(info, edges):
    answer = []
    v = [False] * len(info)
    
    def dfs(s,w):
        if s > w:
            answer.append(s)
        else:
            return
        
        for p, c in edges:
            # 부모 노드는 방문 했고, 자식 노드는 아직 방문 안했다면
            if v[p] and not v[c]:
                v[c] = True
                # 늑대
                if info[c]:
                    dfs(s,w+1)
                # 양
                else:
                    dfs(s+1,w)
                v[c] = False
    # 시작은 양
    v[0] = True
    dfs(1,0)
    return max(answer)