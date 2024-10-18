import sys
input = sys.stdin.readline
N, H = map(int,input().split())

up = [0] * (H+1)
down = [0] * (H+1)

for i in range(1,N+1):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

# 인덱스 역순으로 누적합 계산
for i in range(H-1,0,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]

ans_mn = N
ans_h = 0

for i in range(1,H+1):
    if ans_mn > down[i] + up[H-i+1]:
        ans_mn = down[i] + up[H-i+1]
        ans_h = 1
    elif ans_mn == down[i] + up[H-i+1]:
        ans_h += 1

print(ans_mn,ans_h)