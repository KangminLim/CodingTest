from collections import deque
def solution(people, limit):
    people.sort()
    q = deque(people)
    ans = 0
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
            ans += 1
        else:
            ans += 1
            q.pop()
    if q:
        ans += 1
    return ans