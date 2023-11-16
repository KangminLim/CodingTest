

def solve():
    for lst in arr:
        # 중복을 제거하여 확인
        if len(set(lst)) != N:
            return 0
    # 전치행렬
    arr1 = list(zip(*arr))
    for lst in arr1:
        if len(set(lst)) != N:
            return 0
    for i in range(0,9,3):
        for j in range(0,9,3):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != N:
                return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans =solve()

    print('#{} {}'.format(tc,ans))