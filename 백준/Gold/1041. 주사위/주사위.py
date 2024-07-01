# 주사위
N = int(input())
lst = list(map(int,input().split()))
ans = 0
if N == 1:
    lst.sort()
    print(sum(lst[:-1]))
# elif N == 2:
#     a,b,c = min(lst[0],lst[5]),min(lst[1],lst[4]),min(lst[2],lst[3])
#     ans = (a+b+c) * 4 + (a+b) * 4
#     print(ans)
else:
    min_dice = []
    min_dice.append(min(lst[0],lst[5]))
    min_dice.append(min(lst[1],lst[4]))
    min_dice.append(min(lst[2],lst[3]))
    min_dice.sort()
    a,b,c = min_dice[0], min_dice[1], min_dice[2]
    ans = (a+b+c) * 4 + (a+b) * ((N-1)*4 + (N-2)*4) + a * ((N-2)**2 + 4*(N-2)*(N-1))
    print(ans)

