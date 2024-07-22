from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    summits = set(summits)
    graph = defaultdict(list)
    for u, v, eff in paths:
        graph[u].append((v,eff))
        graph[v].append((u,eff))
    # dijk
    effs = [float('inf')] * (n+1)
    queue = []
    for gate in gates:
        heapq.heappush(queue, (0,gate))
        effs[gate] = 0 
    
    while queue:
        curr_eff, curr = heapq.heappop(queue)
        
        # 두 개 이상의 산봉우리를 방문 x
        if curr in summits:
            continue
        if curr_eff > effs[curr]:
            continue
            
        for neighbor, eff in graph[curr]:
            max_eff = max(curr_eff,eff)
            if max_eff < effs[neighbor]:
                effs[neighbor] = max_eff
                heapq.heappush(queue,(max_eff,neighbor))
    # 최솟값 찾기
    t_summit = intensity = float('inf')
    for summit in summits:
        if effs[summit] < intensity:
            t_summit = summit
            intensity = effs[summit]
        elif effs[summit] == intensity and summit < t_summit:
            t_summit = summit
    return [t_summit,intensity]