N = int(input())
A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort(reverse=True)
S = 0
for i in range(len(A)):
    S += A[i] * B[i]
print(S)