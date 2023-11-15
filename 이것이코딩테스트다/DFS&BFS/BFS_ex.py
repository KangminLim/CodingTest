from collections import deque

def bfs(graph,start,visited):
    queue  =deque([start])
    visited[start] = True
    # queue가 빌 때 까지
    while queue:
        # queue에서 원소 하나 뽑기
        v = queue.popleft()
        print(v,end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [ [],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False] * 9 
bfs(graph,1,visited)