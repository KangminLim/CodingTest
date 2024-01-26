T = int(input())
for tc in range(T):
    N = int(input())
    z_cnt, o_cnt = 1, 0
    for i in range(N):
        z_cnt, o_cnt = o_cnt, z_cnt + o_cnt
    print(z_cnt,o_cnt)