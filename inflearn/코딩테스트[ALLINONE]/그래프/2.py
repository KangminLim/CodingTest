graph = {
    'A' : ['B','D','E'],
    'B' : ['A','C','D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A'],
}
visited = []
def dfs(grpah, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            # visited = dfs(graph,v,visited)
            dfs(v )
    return visited

dfs(graph,'A')