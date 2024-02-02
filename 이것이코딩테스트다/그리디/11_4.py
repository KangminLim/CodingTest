N = int(input())
N_lst = list(map(int,input().split()))
N_lst.sort()
target = 1
for x in N_lst:
    if target < x:
        break
    target += x
print(target)