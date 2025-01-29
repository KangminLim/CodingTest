N = int(input())
lst = list(map(int,input().split()))
L = [0] * N
L[0] = lst[0]
result = L[0]

for i in range(1,N):
    L[i] = max(lst[i], L[i-1]+lst[i])
    result = max(result,L[i])

R = [0] * N
R[-1] = lst[-1]

for i in range(N-2,-1,-1):
    R[i] = max(lst[i],R[i+1] + lst[i])

for i in range(1,N-1):
    result = max(result, L[i-1] + R[i+1])

print(result)