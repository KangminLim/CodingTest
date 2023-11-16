# DFS
def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)
# root만 나한테 주면 root가 가리키는 Tree에 속한 모든 노드에 접근해줄게
dfs(root)