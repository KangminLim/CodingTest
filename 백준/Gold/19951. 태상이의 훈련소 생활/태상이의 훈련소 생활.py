import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
psum = [0] * (N+1)

for _ in range(M):
    a, b, k = map(int, input().split())
    psum[a-1] += k
    psum[b] -= k

for i in range(1,N):
    psum[i] += psum[i-1]
for i in range(N):
    lst[i] += psum[i]
print(*lst)