N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    for j in range(len(lst[i])):
        if j == 0:
            lst[i][j] += lst[i-1][j]
        elif j == len(lst[i])-1:
            lst[i][j] += lst[i-1][j-1]
        else:
            lst[i][j] = max(lst[i-1][j-1],lst[i-1][j])+lst[i][j]

print(max(lst[-1]))