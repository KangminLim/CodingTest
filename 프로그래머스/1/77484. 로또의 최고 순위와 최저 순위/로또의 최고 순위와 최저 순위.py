def solution(lottos, win_nums):
    answer = []
    mn_num, mx_num = 7,7
    for lotto in lottos:
        if lotto == 0:
            mx_num -= 1 
        if lotto in win_nums:
            mx_num -= 1
            mn_num -= 1
    if mx_num == 7:
        mx_num = 6       
    if mn_num == 7:
        mn_num = 6
    return [mx_num, mn_num]