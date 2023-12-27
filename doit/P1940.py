N=int(input())
M =int(input())
A = list(map(int,input().split()))
A.sort()
cnt = 0
i = 0
j = N-1

while i<j: # 투포인터 이동원칙따라 포인터 이동하며 처리
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1 
    else:
        cnt += 1
        i += 1
        j -= 1
        
print(cnt)
    