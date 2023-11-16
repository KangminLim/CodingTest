T=int(input())
for tc in range(1,T+1):
    N, M =map(int,input().split())
    lst1 = list(map(int,input().split()))
    lst2 = list(map(int,input().split()))

    if len(lst1) > len(lst2):
        lst1, lst2 = lst2, lst1

    arr = []

    for i in range(len(lst2)-len(lst1)+1):
        sum = 0
        for j in range(len(lst1)):
            sum += lst1[j] * lst2[j+i]
        arr.append(sum)

    print("#{} {}".format(tc,max(arr)))
