N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(1,N):
    for j in range(N):
        if j > i: break
        # print(i,j)
        if j == 0:
            arr[i][j] = arr[i-1][j] + arr[i][j]
        elif j == i:
            arr[i][j] = arr[i-1][j-1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1],arr[i-1][j]) + arr[i][j]
        # print(arr)
print(max(map(max,arr)))