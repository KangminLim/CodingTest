def solution(s):
    cnt,z_cnt = 0,0
    answer = []
    while True:
        # 1. x의 모든 0을 제거
        new_res = ''
        for i in s:
            if int(i) != 0:
                new_res += i
            else:
                z_cnt += 1
        new_len = len(new_res)

        t = ''
        while new_len >0:
            div = divmod(new_len,2)[0]
            mod = divmod(new_len,2)[1]
            t += str(mod)
            new_len = div
        s = t[::-1]
        cnt += 1
        if s == '1':
            break
    return [cnt,z_cnt]