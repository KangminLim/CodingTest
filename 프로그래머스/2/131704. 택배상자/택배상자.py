from collections import deque
def solution(order):
    answer = 1
    order = deque(order)
    stack = []
    result = []
    size = len(order)
    for i in range(1, size+1):
        stack.append(i) # 박스를 서브 컨테이너에 올리기
        while stack:
            if order and stack[-1] == order[0]: #서브에서 트럭으로
                num = stack.pop()
                order.popleft()
                result.append(num)
            else: # 순서가 잘못된 경우
                break
    return len(result)