N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
flag = list(map(int,input().split()))

def change_arr(arr,flag,N,M):
    if flag == 1:
        narr = [x[:] for x in arr]
        for i in range(N):
            for j in range(M):
                narr[i][j] = arr[N-1-i][j]
    elif flag == 2:
        narr = [x[:] for x in arr]
        for i in range(N):
            for j in range(M):
                narr[i][j] = arr[i][M-1-j]
    elif flag == 3:
        cN, cM = len(arr), len(arr[0])
        narr = [[0] * cN for _ in range(cM)]
        for i in range(cM):
            for j in range(cN):
                narr[i][j] = arr[cN-1-j][i]
        N, M = cM, cN

    elif flag == 4:
        cN, cM = len(arr),len(arr[0])
        narr = [[0] * cN for _ in range(cM)]
        for i in range(cM):
            for j in range(cN):
                narr[i][j] = arr[j][cM-1-i]
        N, M = cM, cN

    elif flag == 5:
        narr = [x[:] for x in arr]
        HN, HM = len(arr) // 2, len(arr[0]) // 2
        for si,sj in ((0,0),(HN,0),(0,HM),(HN,HM)):
            # 4 -> 1
            if (si,sj) == (0,0):
                for i in range(HN):
                    for j in range(HM):
                        narr[si+i][sj+j] = arr[i+HN][j]
            # 3 -> 4
            elif (si, sj) == (HN, 0):
                for i in range(HN):
                    for j in range(HM):
                        narr[si + i][sj + j] = arr[i+HN][j+HM]
            # 2 -> 3
            elif (si,sj) == (HN,HM):
                for i in range(HN):
                    for j in range(HM):
                        narr[si+i][sj+j] = arr[i][j+HM]
            # 1 -> 2
            else:
                for i in range(HN):
                    for j in range(HM):
                        narr[si+i][sj+j] = arr[i][j]

    elif flag == 6:
        narr = [x[:] for x in arr]
        HN, HM = len(arr) // 2, len(arr[0]) // 2
        for si, sj in ((0, 0), (HN, 0), (0, HM), (HN, HM)):
            # 2 -> 1
            if (si, sj) == (0, 0):
                for i in range(HN):
                    for j in range(HM):
                        narr[si + i][sj + j] = arr[i][j+HM]
            # 1 -> 4
            elif (si, sj) == (HN, 0):
                for i in range(HN):
                    for j in range(HM):
                        narr[si + i][sj + j] = arr[i][j]
            # 4 -> 3
            elif (si, sj) == (HN, HM):
                for i in range(HN):
                    for j in range(HM):
                        narr[si + i][sj + j] = arr[i+HN][j]
            # 3 -> 2
            else:
                for i in range(HN):
                    for j in range(HM):
                        narr[si + i][sj + j] = arr[i+HN][j+HM]

    return narr, N, M

for i in range(R):

    arr,N,M = change_arr(arr,flag[i],N,M)

for i in arr:
    print(*i)

