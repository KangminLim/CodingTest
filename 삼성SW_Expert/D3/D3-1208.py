for tc in range(1,11):
    dump = int(input())
    box_list = list(map(int,input().split()))
    box_list.sort()
    answer= 0
    for i in range(dump):
        box_list.sort()
        answer = box_list[-1] - box_list[0]
        box_list[0] = box_list[0] + 1
        box_list[-1] = box_list[-1] -1
        if answer < box_list[-1] - box_list[0]:
            break
    box_list.sort()
    answer = box_list[-1] - box_list[0]
    print('#{} {}'.format(tc,answer))
