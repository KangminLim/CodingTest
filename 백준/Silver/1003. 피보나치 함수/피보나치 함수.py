T = int(input())
for _ in range(T):
    tc = int(input())
    if tc == 0:
        print(1, 0)
        continue
    elif tc == 1:
        print(0, 1)
        continue
    z_cnt, o_cnt = 1, 1
    for _ in range(2,tc):
        z_cnt, o_cnt = o_cnt, o_cnt+z_cnt
    print(z_cnt, o_cnt)