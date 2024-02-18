from collections import deque

def BFS(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

graph = {
    'A' : ['B','D','E'],
    'B' : ['A','C','D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],

}
BFS(graph, 'A')