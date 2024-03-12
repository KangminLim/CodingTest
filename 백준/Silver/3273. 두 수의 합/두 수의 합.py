import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
x = int(input())

i = 0
j = len(lst)-1
cnt = 0
while i < j:

    if lst[i] + lst[j] < x:
        i += 1
    elif lst[i] + lst[j] > x:
        j -= 1
    else:
        i += 1
        cnt += 1
print(cnt)