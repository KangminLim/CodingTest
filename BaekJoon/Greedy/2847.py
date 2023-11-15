N = int(input())
scores = [int(input()) for _ in range(N)]

cnt = 0 
for i in range(N-2, -1 , -1):
    if scores[i] >= scores[i+1]:
        decrease = scores[i] - scores[i+1] + 1 
        scores[i] -= decrease
        cnt += decrease
print(cnt)
