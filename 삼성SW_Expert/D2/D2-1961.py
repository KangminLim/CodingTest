# 회전 및 반전은 좌표를 기준으로 풀자 / 목적지 기준으로 저장
T =int(input())

def rotation(a,N):
    new_lst = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_lst[i][j] = a[N-1-j][i]
    return new_lst


for tc in range(1,T+1):
    N = int(input())
    lst = [list(map(str,input().split())) for _ in range(N) ]

    rot_90 = rotation(lst,N)
    rot_180 =rotation(rot_90,N)
    rot_270 = rotation(rot_180,N)

    print(f'#{tc}')
    for a,b,c in zip(rot_90,rot_180,rot_270):
        a1 =''.join(a)
        b1 =''.join(b)
        c1 =''.join(c)
        print(a1,b1,c1)

