N = int(input())
Vs = list(map(int, input().split()))
V = 1
s = V
for i in range(N-1):
    V = (min([V+1,Vs[-2-i]]))
    s += V
print(s)