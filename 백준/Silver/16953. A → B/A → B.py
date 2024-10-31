from collections import deque
start, target = map(int,input().split())
def bfs(start):
    q = deque()
    q.append((start,1))
    while q:
        cur,cnt = q.popleft()
        if cur == target:
            print(cnt)
            return
        if 2*cur <= target:
            q.append((2*cur,cnt+1))
        if 10*cur + 1 <= target:
            q.append((10*cur+1,cnt+1))
    print(-1)
bfs(start)