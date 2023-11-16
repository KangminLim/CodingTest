def inorder(cur_node):
    if cur_node is None:
        return
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

inorder(root)