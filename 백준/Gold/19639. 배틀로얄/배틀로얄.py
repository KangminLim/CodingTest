X,Y,M = map(int,input().split())
enemy = [int(input()) for _ in range(X)]
heal = [int(input()) for _ in range(Y)]

e_idx = h_idx = 0
init_M = M
ans = []

if M + sum(heal) <= sum(enemy):
    print(0)
else:
    for _ in range(X+Y):

        if M > init_M//2 and enemy:
            M -= enemy[e_idx]
            e_idx += 1
            ans.append(-e_idx)
        elif M <= init_M//2 and heal:
            M += heal[h_idx]
            h_idx += 1
            ans.append(h_idx)

        if e_idx == X and h_idx != Y:
            while h_idx < Y:
                M += heal[h_idx]
                h_idx += 1
                ans.append(h_idx)
            break

    if len(ans) == X+Y:
        for a in ans:
            print(a)
    else:
        print(0)