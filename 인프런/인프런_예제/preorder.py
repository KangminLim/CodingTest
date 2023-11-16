# 전위 순회 Preorder : 자식들보고 순회하라고 하기전에 부모가 먼저 하는 것
def preorder(cur_node):
    if cur_node is None:
        return

    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

preorder(root)