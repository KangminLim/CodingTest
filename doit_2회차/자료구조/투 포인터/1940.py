#주몽의 명령
N = int(input())
M = int(input())
A = list(map(int,input().split()))
A.sort()
i = 0
j = N - 1
count = 0
while i<j:
    sum = A[i] +A[j]
    if sum < M : i += 1
    elif sum > M : j-=1
    else:
        count+= 1
        i+= 1
        j-=1
print(count)