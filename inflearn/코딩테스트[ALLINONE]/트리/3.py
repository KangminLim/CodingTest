def dfs(root):
    if root is None:
        return
    dfs(root.left)
    dfs(root.right)
dfs(root)