graph={
    'A':['B','D','E'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['A','B'],
    'E':['A']
}
visited=[]
#외워라 좀
# def dfs(graph, cur_v, visited=[]):
#     visited.append(cur_v)
#     for v in graph[cur_v]:
#         if v not in visited:
#             visited = dfs(graph,v,visited)
#     return visited
#
# dfs(graph,'A')

def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)
dfs('A')
