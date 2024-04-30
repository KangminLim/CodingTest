N = int(input())
nlst = list(map(int,input().split()))
result = [1] * (N+1)
result[1] = nlst[N-1]

for i in range(2,N+1):
    result[i] = result[i-1] * nlst[N-i] + result[i-2]
print(result[N] - result[N-1],result[N])