N, K = map(int,input().split())

time = [-1] * 100001

from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    time[start] = 0
    while q:
        cur = q.popleft()
        if cur == K:
            return

        for next in (cur*2,cur-1,cur+1):
            if 0<=next<=100000 and time[next] == -1:
                if next == cur*2:
                    time[next] = time[cur]
                    q.appendleft(next)
                else:
                    time[next] = time[cur] + 1
                    q.append(next)
bfs(N)
print(time[K])