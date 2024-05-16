N=4
arr= [[0]*8]+[list(map(int,input())) for _ in range(N)]
K =int(input())
top = [0]*(N+1)

for _ in range(K):
    idx, dr = map(int,input().split())
    # [1] idx 톱니를 회전
    tlst = [(idx,0)]
    # [2] idx 우측 방향처리 (같은 극성 나오면 탈출)
    for i in range(idx+1,N+1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 => 회전후보 추가
        if arr[i-1][(top[i-1]+2)%8] != arr[i][(top[i]+6)%8]:
            tlst.append((i,(i-idx)%2))
        else:
            break

    for i in range(idx-1,0,-1):
        # 왼쪽 3시 극성 != 오른쪽 9시 극성 -> 회전후보 추가
        if arr[i][(top[i]+2)%8] != arr[i+1][(top[i+1]+6)%8]:
            tlst.append((i,(idx-i)%2))
        else:
            break
    # [4] 실제 회전 처리(cw이면 top값을 -1)
    for i, rot in tlst:
        if rot == 0:
            top[i] = (top[i]-dr+8)%8
        else:
            top[i] = (top[i]+dr+8)%8

ans = 0
tbl = [0,1,2,4,8]
for i in range(1,N+1):
    ans += arr[i][top[i]] * tbl[i]
print(ans)