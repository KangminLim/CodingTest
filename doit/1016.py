# 제곱이 아닌 수
import math
Min, Max = map(int,input().split())
Check = [False] * (Max-Min+1)

for i in range(2, int(math.sqrt(Max)+1)):
    pow = i*i
    start_idx = int(Min/pow)
    if Min % pow != 0:
        #나머지가 있는 경우 1을 더해 Min보다 큰 제곱수에서 시작하도록 설정
        start_idx +=1
    for j in range(start_idx, int(Max/pow)+1):
        Check[int((j*pow)-Min)] = True

cnt = 0

for i in range(0, Max-Min+1):
    if not Check[i]:
        cnt += 1

print(cnt)