import sys
input = sys.stdin.readline
N = int(input())
M = []
D = [[-1 for j in range(N+1)] for i in range(N+1)]

M.append((0,0))

for i in range(N):
    x, y = map(int,input().split())
    M.append((x,y))

def execute(s,e): # 탑-다운 방식 점화식 함수
    result = sys.maxsize
    if D[s][e] != -1: # 이미 계산한 부분은 다시 계산하지 않음(메모이제이션)
        return D[s][e]
    if s == e:
        return 0
    if s+1==e:
        return M[s][0] * M[s][1] * M[e][1]
    for i in range(s,e):
        result = min(result,M[s][0]*M[i][1]*M[e][1] + execute(s,i) + execute(i+1,e))
    D[s][e] = result
    return D[s][e]

print(execute(1,N))