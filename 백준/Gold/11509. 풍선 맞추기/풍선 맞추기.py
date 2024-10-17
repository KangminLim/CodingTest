N = int(input())
lst = list(map(int,input().split()))
positions = [0] * (1000001)

for i in range(len(lst)):
    # print(lst[i],lst[i-1])
    if positions[lst[i]] == 0:
        positions[lst[i]-1] += 1
    else:
        positions[lst[i]-1] += 1
        positions[lst[i]] -= 1
print(sum(positions))