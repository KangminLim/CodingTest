import heapq

def dijkstra(start, distance, graph):
    
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: # 이미 최단거리 갱신된거면 건너뛰기
            continue
        
        for connect_info in graph[now]: # 연결된 친구들 찾기 #now를 거쳐서 가는게 최단거리일 경우 갱신해주기 위함
            new_dist = dist + connect_info[1] # cost
            
            if new_dist < distance[connect_info[0]]: # 해당 노드까지의 거리보다 새롭게 계산한 거리가 짧으면
                distance[connect_info[0]] = new_dist
                heapq.heappush(q, (new_dist,connect_info[0]))
                
    

def solution(N, road, K):
    # 1번 노드에서 전체 노드까지의 최단 거리를 찾아야한다.(다익스트라)
    # heapq 사용
    
    distance = [int(1e9)] * (N+1)

    graph = [[] for _ in range(N+1)]
    
    for a,b,cost in road:
        graph[a].append((b,cost))
        graph[b].append((a,cost))
    
    dijkstra(1,distance,graph)
    
    answer = 0
    for i in range(1,N+1):
        if distance[i] <= K:
            answer += 1
    
    return answer