N = int(input())
A = [[0]*2 for _ in range(N)]

for i in range(N):
    S, E = map(int,input().split())
    A[i][0] = E #종료 시각 우선 정렬이 먼저이므로 0번째에 종료 시각을 먼저 저장
    A[i][1] = S
    
A.sort()
count = 0
end = -1

for i in range(N):
    if A[i][1] >= end:
        end = A[i][0] 
        count += 1
print(count)