T = int(input())
from collections import deque
def fbfs(flst):
    v1 = [[-1] * (w+2) for _ in range(h+2)]
    for fi,fj in flst:
        v1[fi][fj] = 0
    q = deque(flst)
    while q:
        ci,cj = q.popleft()
        for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
            if v1[ni][nj] == -1 and arr[ni][nj] == '.':
                v1[ni][nj] = v1[ci][cj] + 1
                q.append((ni,nj))
    return v1

def sbfs(si,sj):
    v2 = [[-1] * (w+2) for _ in range(h+2)]
    v2[si][sj] = 0
    q = deque()
    q.append((si,sj))
    while q:
        ci,cj = q.popleft()

        for ni, nj in ((ci - 1, cj), (ci, cj + 1), (ci + 1, cj), (ci, cj - 1)):
            if v2[ni][nj] == -1 and arr[ni][nj] == '.' and (v1[ni][nj] == -1 or v2[ci][cj]+1 < v1[ni][nj]):
                q.append((ni,nj))
                v2[ni][nj] = v2[ci][cj] + 1
            if not (1 <= ni <= h and 1 <= nj <= w):
                return v2[ci][cj] + 1,v2
    return False,v2

for tc in range(T):
    w, h = map(int,input().split())
    arr = [['#'] * (w+2)] + [['#'] + list(map(str,input())) + ['#'] for _ in range(h)] + [['#'] * (w+2)]
    flst = []
    for i in range(1,h+2):
        for j in range(1,w+2):
            if arr[i][j] == '@':
                si,sj = i,j
                arr[i][j] = '.'
            elif arr[i][j] == '*':
                flst.append((i,j))

    v1 = fbfs(flst)
    ans,v2 = sbfs(si,sj)
    if ans: print(ans)
    else: print('IMPOSSIBLE')


