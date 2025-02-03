from collections import deque
N, L = map(int,input().split())
q = deque()
lst = list(map(int,input().split()))

for i in range(N):
    while q and q[-1][0] > lst[i]:
        q.pop()
    q.append((lst[i],i))
    if q[0][1] <= i-L:  # 범위에서 벗어난 값은 덱에서 제거
        q.popleft()
    print(q[0][0],end = ' ')

