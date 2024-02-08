# 문자열 재정렬(facebook 인터뷰)
S = list(input())
S.sort()
S_alpha = ''
S_num = 0
S_final = ''
for i in range(len(S)):
    if S[i].isdigit():
        S_num += int(S[i])
    else:
        S_alpha += S[i]

S_final += S_alpha
S_final += str(S_num)
print(S_final)