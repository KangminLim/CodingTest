cost = [(k*k +(k-1)*(k-1)) for k in range(40)]
def solve():
    ans = 0
    for si in range(N):
        for sj in range(N): # 모든 시작위치
            for k in range(1,2*N):
                cnt = 0
                for i in range(si-k+1,si+k):
                    for j in range(sj-k+1+abs(i-si),sj+k-abs(i-si)):
                        # 범위내이고 집인경우 count
                        if 0<=i<N and 0<=j<N and arr[i][j]:
                            cnt += 1
                if cost[k] <= cnt*K  and ans <cnt:
                    ans = cnt
    return ans

def solve1():
    ans = 0
    # [1] home 배열 생성
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                home.append((i,j))
    # [2] 모든좌표 순회하면서, dist배열 생성
    for si in range(N):
        for sj in range(N):
            dist = [0]*40
            for hi,hj in home:
                t = abs(si-hi) + abs(sj-hj) + 1
                dist[t] +=1
            cnt=0
            for k in range(1,40):
                cnt += dist[k]
                if cost[k] <= cnt * K and ans < cnt:
                    ans =cnt
    return ans

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = solve1()
    print(f'{test_case} {ans}')