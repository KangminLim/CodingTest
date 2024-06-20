roma = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
special_roma = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

i_roma = [str(input()) for _ in range(2)]
ans = 0
for r in i_roma:
    sm = 0
    tmp_ch = ''
    V_flag, L_flag, D_flag = False, False, False
    I_cnt, X_cnt, C_cnt, M_cnt = 0, 0, 0, 0
    IV_flag, IX_flag, XL_flag, XC_flag, CD_flag, CM_flag = False, False, False, False, False, False
    continue_flag = False
    for i in range(len(r)):
        if continue_flag:
            continue_flag = False
            continue

        if i < len(r)-1:
            if (r[i] + r[i+1]) in special_roma:
                tmp = r[i] + r[i+1]
                if tmp == 'IV' and not IV_flag and not IX_flag:
                    IV_flag = True
                    I_cnt += 1
                    V_flag = True
                    sm += special_roma[tmp]
                    continue_flag = True
                elif tmp == 'IX' and not IX_flag and not IV_flag :
                    IX_flag = True
                    I_cnt += 1
                    X_cnt += 1
                    sm += special_roma[tmp]
                    continue_flag = True
                elif tmp == 'XL' and not XL_flag and not XC_flag:
                    XL_flag = True
                    X_cnt += 1
                    L_flag = True
                    sm += special_roma[tmp]
                    continue_flag = True
                elif tmp == 'XC' and not XC_flag and not XL_flag:
                    XC_flag = True
                    X_cnt += 1
                    C_cnt += 1
                    sm += special_roma[tmp]
                    continue_flag = True
                elif tmp == 'CD' and not CD_flag and not CM_flag:
                    CD_flag = True
                    C_cnt += 1
                    D_flag = True
                    sm += special_roma[tmp]
                    continue_flag = True
                elif tmp == 'CM' and not CM_flag and not CD_flag:
                    CM_flag = True
                    C_cnt += 1
                    M_cnt += 1
                    sm += special_roma[tmp]
                    continue_flag = True

            else:
                tmp = r[i]

                if tmp =='V' and not V_flag:
                    V_flag = True
                    sm += roma[tmp]
                elif tmp == 'L' and not L_flag:
                    L_flag = True
                    sm += roma[tmp]
                elif tmp == 'D' and not D_flag:
                    D_flag = True
                    sm += roma[tmp]
                elif tmp =='I' and I_cnt < 3:
                    I_cnt += 1
                    sm += roma[tmp]
                elif tmp == 'X' and X_cnt < 3:
                    X_cnt += 1
                    sm += roma[tmp]
                elif tmp == 'C' and C_cnt < 3:
                    C_cnt += 1
                    sm += roma[tmp]
                elif tmp == 'M' and M_cnt < 3:
                    M_cnt += 1
                    sm += roma[tmp]
        else:
            tmp = r[i]

            if tmp == 'V' and not V_flag:
                V_flag = True
                sm += roma[tmp]
            elif tmp == 'L' and not L_flag:
                L_flag = True
                sm += roma[tmp]
            elif tmp == 'D' and not D_flag:
                D_flag = True
                sm += roma[tmp]
            elif tmp == 'I' and I_cnt < 3:
                I_cnt += 1
                sm += roma[tmp]
            elif tmp == 'X' and X_cnt < 3:
                X_cnt += 1
                sm += roma[tmp]
            elif tmp == 'C' and C_cnt < 3:
                C_cnt += 1
                sm += roma[tmp]
            elif tmp == 'M' and M_cnt < 3:
                M_cnt += 1
                sm += roma[tmp]
    ans += sm

print(ans)
ans_ch = ''

V_flag, L_flag, D_flag = False, False, False
I_cnt, X_cnt, C_cnt, M_cnt = 0,0,0,0
IV_flag,IX_flag,XL_flag,XC_flag,CD_flag,CM_flag = False, False, False, False, False, False

while ans >0:
    if ans >= 1000 and M_cnt <3:
        ans_ch += 'M'
        ans-=1000
        M_cnt += 1
    elif ans >= 900 and not CM_flag and not CD_flag:
        ans_ch += 'CM'
        ans -= 900
        CM_flag = True
        C_cnt += 1
        M_cnt += 1
    elif ans >= 500 and not D_flag:
        ans_ch += 'D'
        ans -= 500
        D_flag = True
    elif ans >= 400 and not CD_flag and not CM_flag:
        ans_ch += 'CD'
        ans -= 400
        CD_flag = True
        C_cnt += 1
        D_flag = True
    elif ans >= 100 and C_cnt < 3:
        ans_ch += 'C'
        ans -= 100
        C_cnt += 1
    elif ans >= 90 and not XC_flag and not XL_flag:
        ans_ch += 'XC'
        ans -= 90
        XC_flag = True
        X_cnt += 1
        C_cnt += 1
    elif ans >= 50 and not L_flag:
        ans_ch += 'L'
        ans -= 50
        L_flag = True
    elif ans >= 40 and not XC_flag and not XL_flag:
        ans_ch += 'XL'
        ans -= 40
        XL_flag = True
        X_cnt += 1
        L_flag = True
    elif ans >= 10 and X_cnt < 3:
        ans_ch += 'X'
        ans -= 10
        X_cnt += 1
    elif ans >= 9 and not IX_flag and not IV_flag:
        ans_ch += 'IX'
        ans -= 9
        IX_flag = True
        I_cnt += 1
        X_cnt += 1
    elif ans >= 5 and not V_flag:
        ans_ch += 'V'
        ans -= 5
        V_flag = True
    elif ans >= 4 and not IV_flag and not IX_flag:
        ans_ch += 'IV'
        ans -= 4
        IV_flag = True
        I_cnt += 1
        V_flag = True
    elif ans >= 1 and I_cnt < 3:
        ans_ch += 'I'
        ans -= 1
        X_cnt += 1

print(ans_ch)