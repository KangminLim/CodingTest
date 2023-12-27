N = int(input())
A = []
for i in range(N):
    A.append((int(input()),i)) # 정렬 기준을 고려하여 데이터, index 순서로 저장

Max = 0 
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i : #정렬 전 index -정렬 후 index 결과값 저장
        Max = sorted_A[i][1]-i

print(Max+1)