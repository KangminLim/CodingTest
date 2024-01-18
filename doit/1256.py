# 사전
import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
D = [[0 for j in range(202)] for i in range(202)]

for i in range(0,201): # 조합 테이블 만들기
    for j in range(0, i+1):
        if j == 0 or j == i:
            D[i][j] = 1
        else:
            D[i][j] = D[i-1][j-1] + D[i-1][j]
            if D[i][j] > 1000000000:
                D[i][j] = 1000000001 # K 범위가 넘어감녀 범위의 최댓값 저장

if D[N+M][M] < K: # 주어진 자릿수로 만들 수 없는 K번째 수의 경우
    print(-1)

else:
    while not (N==0 and M ==0):
        if D[N-1+M][M] >= K:
            print('a', end='')
            N -= 1
        else:
            print('z', end='')
            K -= D[N-1+M][M]
            M -= 1
