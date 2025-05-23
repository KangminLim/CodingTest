# 선물 전달
N = int(input())
mod = 1000000000
D = [0] * 10000001
D[1] = 0
D[2] = 1

for i in range(3, N+1):
    D[i] = (i-1) * (D[i-1] + D[i-2]) % mod #완전 순열 점화식

print(D[N])
