import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
M = int(input())
tlst = list(map(int,input().split()))

def binary_search(start,end,target):

    while start <= end:
        mid = (start+end)//2
        if lst[mid] == target:
            print(1)
            return
        elif lst[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    print(0)
    return

for target in tlst:
    binary_search(0,N-1,target)