from collections import deque
def solution(priorities, location):
    q = deque()
    answer = 0
    for idx, val in enumerate(priorities):
        q.append((val,idx))
        
    while q:
        item = q.popleft()
        if q and item[0] < max(q)[0]:
            q.append(item)
        else:
            answer += 1
            if item[1] == location:
                break

    return answer