# 유기농 배추
T = int(input())
for tc in range(T):
    M,N,K = map(int,input().split ())
    mp = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        for i in range(N):
            x, y = map(int, input().split())
            for j in range(M):
                mp[x][y] = 1
    print(mp)
