N, K = map(int,input().split())
A= [0] * N

for i in range(N):
    A[i] = int(input())

cnt = 0

for i in range(N-1, -1, -1):
    if A[i] <= K:
        cnt += int(K/A[i])
        K= K % A[i]
print(cnt)