for _ in range(1,11):
    tc = _
    result = 0
    N = int(input())
    building_list = list(map(int,input().split()))
    for i in range(2,N-2):
        argmax = max(building_list[i-2],building_list[i-1],building_list[i+1],building_list[i+2])
        if argmax<building_list[i]:
            result += building_list[i]-argmax
    print('#{} {}'.format(tc,result))