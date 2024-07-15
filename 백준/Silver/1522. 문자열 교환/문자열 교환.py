s = str(input())
acnt = s.count('a')
answer = int(1e9)

i = 0
slen = len(s)
# print(slen)
while i < slen:
    j = i + acnt
    if j > slen:
        # print(s[i:slen],s[:j-slen])
        tmp = s[i:slen] + s[:j-slen]
        # print(tmp,i,j)
    else:
        tmp = s[i:j]

    answer = min(answer,tmp.count('b'))
    i += 1
print(answer)