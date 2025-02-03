import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
prefix_sum = [0] * (N+1)

for i in range(1,N+1):
    prefix_sum[i] = lst[i-1] + prefix_sum[i-1]

for _ in range(M):
    s,e = map(int,input().split())
    print(prefix_sum[e] - prefix_sum[s-1])