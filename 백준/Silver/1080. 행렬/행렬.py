N, M = map(int,input().split())
alst = [list(map(int,input())) for _ in range(N)]
blst = [list(map(int,input())) for _ in range(N)]
cnt = 0

def convert_arr(arr,si,sj):
    for i in range(3):
        for j in range(3):
            if arr[si+i][sj+j] == 1:
                arr[si+i][sj+j] = 0
            else:
                arr[si+i][sj+j] = 1
for i in range(N-2):
    for j in range(M-2):
        if alst[i][j] != blst[i][j]:
            convert_arr(alst,i,j)
            cnt += 1

flag = True

for i in range(N):
    for j in range(M):
        if alst[i][j] != blst[i][j]:
            flag = False
            break
    if not flag: break

if flag: print(cnt)
else: print(-1)
    