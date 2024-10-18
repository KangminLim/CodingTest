import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i,j,dr):
    global ans
    # 끝 좌표에 도달하면 정답 업데이트
    if i==N-1 and j==N-1:
        ans += 1
        return
    # 오른쪽 밀기
    if dr == 0 or dr == 2:
        # 범위 내, 빈칸
        if j+1 < N and arr[i][j+1] == 0:
            dfs(i,j+1,0)

    if dr == 1 or dr == 2:
        # 범위 내, 빈칸
        if i+1 < N and arr[i+1][j] == 0:
            dfs(i+1,j,1)
    # 아래로 밀기
    # 오른쪽 or 아래로 이동 불가 -> 대각선 이동/
    # 범위내 / 빈칸 조건
    if i+1 < N and j+1 < N and arr[i+1][j] == 0 and arr[i][j+1] == 0 and arr[i+1][j+1] == 0:
        dfs(i+1,j+1,2)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
dfs(0,1,0)
print(ans)