# 마법사 상어와 파이어볼

N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(M)]

di,dj = [-1,-1,0,1,1,1,0,-1], [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    # [0]:i, [1]:j, [2]:질량, [3]:속도, [4]:방향
    # [1] 개체별 이동 (파이어볼)
    for i in range(len(arr)): # 개수가 사라져서 arr로
        arr[i][0] = (arr[i][0] + di[arr[i][4]]*arr[i][3])%N + 1
        arr[i][1] = (arr[i][1] + dj[arr[i][4]] * arr[i][3]) % N + 1

    # [2] 전체 개체 정렬(좌표 기준으로 정렬 => 같은 좌표 처리)
    arr.sort(key=lambda x:(x[0],x[1]))
    arr.append([100,100,0,0,0]) # 패딩처리 : 마지막 요소 처리를 위한 인덱스
    new = []

    # [3] 같은 좌표 합치고(2개 이상) + 나누고(2개 이상) => new에 추가
    i = 0
    while i<len(arr)-1:
        si, sj, m, s, d = arr[i]  # 기준 좌표
        start = 0 # 같으면 0,2,4,8
        for j in range(i+1,len(arr)):
            if (si,sj) == (arr[j][0],arr[j][1]): # 같은 좌표면 합치기
                m += arr[j][2]
                s += arr[j][3]
                if d%2 != arr[j][4]%2: # 다른 방향 start = 1
                    start = 1

            else: # 다른 좌표!
                if j-i == 1: # 1개 => 그냥 추가
                    new.append(arr[i])
                else: # 여러개
                    if m//5>0: # 나눠도 1 이상이면
                        for dr in range(start,start+8,2):
                            new.append([si,sj,m//5,s//(j-i),dr])
                break
        i = j
    arr = new

ans= 0

for lst in arr:
    ans += lst[2]

print(ans)