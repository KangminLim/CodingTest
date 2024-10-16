def solution(tickets):
    answer = []
    v = [False] * len(tickets)
    
    def dfs(cur,tlst):
        if len(tlst) == len(tickets)+1:
            answer.append(tlst)
            return
        
        for idx, ticket in enumerate(tickets):
            if not v[idx] and cur == ticket[0]:
                v[idx] = True
                dfs(ticket[1], tlst+[ticket[1]])
                v[idx] = False
        
    dfs("ICN",["ICN"])
    answer.sort()
    return answer[0]
    
