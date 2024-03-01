# 부품 찾기
N = int(input())
arr = list(map(int,input().split()))
arr.sort()

def binary_search(array,target, start,end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

M = int(input())
target_lst = list(map(int,input().split()))
target_lst.sort()

for i in range(M):
    target = target_lst[i]
    result = binary_search(arr,target,0,N-1)
    if result == None:
        print("NO",end=' ')
    else:
        print("YES",end=' ')

# for i in target_lst:
#     result = binary_search(arr, i, 0, n - 1)
#     if result == None:
#         print("NO", end=' ')
#     else:
#         print("YES", end=' ')