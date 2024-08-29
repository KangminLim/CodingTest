M,N = map(int,input().split())
n = int(input())
lst = []
# arr = [[0] * (M+1) for _ in range(N+1)]
for idx in range(1,n+1):
    cd, mul = map(int,input().split())
    if cd == 1:
        cpos = M - mul
        lst.append(cpos)
        # arr[0][mul] = idx
        # lst.append((0,mul))
    elif cd == 2:
        cpos = M + N + mul
        lst.append(cpos)
        # arr[N][mul] = idx
        # lst.append((N,mul))
    elif cd == 3:
        cpos = M + mul
        lst.append(cpos)
        # arr[mul][0] = idx
        # lst.append((mul,0))
    elif cd == 4:
        cpos = M + N + M + N - mul
        lst.append(cpos)
        # arr[mul][N] = idx
        # lst.append((mul,N))
# 동근
cd, mul = map(int,input().split())
if cd == 1:
    dpos = M - mul
elif cd == 2:
    dpos = M + N + mul
elif cd == 3:
    dpos = M + mul
elif cd == 4:
    dpos = M + N + M + N - mul

ans = 0

for idx in range(n):
    cpos = lst[idx]
    dist1 = abs(dpos-cpos)
    dist2 = N * 2 + M * 2 - dist1
    ans += min(dist1, dist2)
print(ans)

# from collections import deque
# def bfs(si,sj,ei,ej):
#     q = deque()
#     q.append((si,sj))
#     v = [[False] * (M+1) for _ in range(N+1)]
#     v[si][sj] = True
#     cnt = 0
#     while q:
#         ci,cj = q.popleft()
#         if (ci,cj) == (ei,ej):
#             return cnt
#         for ni, nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
#             if ((ni==0 or ni==N) and 0<=nj<M) or (0<=ni<=N and (nj==0 or nj==M)) and not v[ni][nj]:
#                 q.append((ni,nj))
#                 v[ni][nj] = True
#                 cnt += 1

