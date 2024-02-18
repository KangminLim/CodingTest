from collections import deque
queue = deque()
# enquue() O(1)
queue.append(1)
# dequeue() O(1)
queue.popleft()

stack = []
# push O(1)
stack.append(1)
# pop O(1)