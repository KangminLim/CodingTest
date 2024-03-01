# 고정점 찾기
def binary_search(array,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] >= mid:
        return binary_search(array,start,mid-1)
    else:
        return binary_search(array,mid+1,end)

N = int(input())
arr = list(map(int,input().split()))

index = binary_search(arr, 0, N-1)

if index == None:
    print(-1)
else:
    print(index)