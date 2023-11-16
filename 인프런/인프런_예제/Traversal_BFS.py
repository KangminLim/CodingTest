# BFS 초기세팅 외워야함
from collections import deque

def bfs(root):
    # 방문해서 action을 취한 것 -> cur_node에 방문해서 depth를 알아보는 것
    visited=[]
    if root is None:
        return 0
    # FIFO que를 구현하기 위해 deque
    q = deque()
    # 접근
    q.append(root)
    while q:
        # 접근한 상태
        cur_node=q.popleft()
        # 방문한 노드의 value값을 남겨 방문 기록 작성
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

bfs(root)
