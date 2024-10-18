def solution(n, results):
    graph = [[] for _ in range(n+1)]  # 이긴 선수 기록
    reverse_graph = [[] for _ in range(n+1)]  # 진 선수 기록
    
    # 그래프에 결과를 반영 (단방향)
    for a, b in results:
        graph[a].append(b)  # a 선수가 b 선수를 이김
        reverse_graph[b].append(a)  # b 선수가 a 선수에게 패배
    
    def dfs(start, graph, visited):
        stack = [start]
        visited[start] = True
        count = 0
        
        while stack:
            cur = stack.pop()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
                    count += 1
        return count

    answer = 0

    # 각 선수를 기준으로 자신보다 강한 선수와 약한 선수의 수를 계산
    for i in range(1, n+1):
        visited_win = [False] * (n+1)
        visited_lose = [False] * (n+1)
        
        # i 선수가 이긴 선수들을 탐색
        win_count = dfs(i, graph, visited_win)
        # i 선수가 진 선수들을 탐색
        lose_count = dfs(i, reverse_graph, visited_lose)
        
        # 자신보다 강하거나 약한 선수를 모두 알면 순위를 매길 수 있음
        if win_count + lose_count == n - 1:
            answer += 1
    
    return answer
