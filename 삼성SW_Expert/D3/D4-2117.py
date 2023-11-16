# def solve():
#     ans = 0
#     for si in range(N):
#         for sj in range(N): # 모든 시작위치
#             for k in range(1,2*N):
#                 cnt = 0
#                 for i in range(si-k+1,si+k):
#                     for j in range(sj-k+1+abs(i-si),sj+k-abs(i-si)):
#                         # 범위내이고 집인경우 count
#                         if 0<=i<N and 0<=j<N and arr[i][j]:
#                             cnt += 1
#                 cost = k*k+(k-1)*(k-1)
#                 if cost <= cnt*K  and ans <cnt:
#                     ans = cnt
#
# T = int(input())
# for test_case in range(1,T+1):
#     N, K = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#
#     ans = solve()
#     print(f'{test_case} {ans}')

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

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    ans = solve()
    print(f'{test_case} {ans}')