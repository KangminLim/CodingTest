T = int(input())

for tc in range(1,T+1):
    S = list(map(int,input().split()))
    result, S_min, S_max = 0,0,0
    S_min, S_max = min(S),max(S)
    S.remove(S_min)
    S.remove(S_max)
    for i in S:
        result += i
    result = round(result/len(S))
    print('#{} {}'.format(tc,result))