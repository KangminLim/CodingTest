from collections import deque

def solution(people, limit):
    people.sort()
    q = deque(people)
    answer = 0
    cur_limit = 0
    while len(q)>1:
        if q[-1] + q[0] <= limit:
            q.popleft()
            q.pop()
            answer += 1
        else:
            q.pop()
            answer += 1
    if q:
        answer += 1
    return answer