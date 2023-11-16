N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def cal(tlst):
    # 모든 집과 tlst의 치킨집 거리중 최솟값의 누적값 구하기
    sm = 0
    for hi,hj in home: # 집 좌표를 하나씩 처리
        mn = 2*N
        for ci,cj in tlst:
            mn = min(mn, abs(hi-ci)+abs(hj-cj))
        sm += mn
    return sm

def dfs(n,tlst):
    global ans
    if len(tlst)+(CNT-n)<M:
        return
    if len(tlst)>M:
        return
    if n ==CNT:                 # 종료조건 : 모든 치킨집의 폐업여부 결정
        if len(tlst) == M:      # M개 유지 결정시 최솟값 갱신
            ans = min(ans,cal(tlst))
        return

    dfs(n+1,tlst+[chicken[n]]) # 유지하는 경우
    dfs(n+1,tlst) # 폐업하는 경우

# [1] 집, 치킨집 좌표를 hoem,chicken[] 에 저장

home =[]
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i,j))
        elif arr[i][j] == 2:
            chicken.append(((i,j)))
CNT = len(chicken)

ans = 2*N*2*N # 최대 2N개의 집이 가장 멀리 있을 때
dfs(0, [])
print(ans)