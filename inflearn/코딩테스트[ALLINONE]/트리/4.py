def preorder(cur_node):
    if cur_node is None:
        return

    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

def inorder(cur_node):
    if cur_node is None:
        return

    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)
inorder(root)

def postorder(cur_node):
    if cur_node is None:
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)
postorder(root)