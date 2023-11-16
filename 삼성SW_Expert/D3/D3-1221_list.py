T = int(input())
dic = {'ZRO' : 0, 'ONE' : 1,'TWO' : 2, 'THR':3,'FOR' :4,'FIV':5,'SIX':6,'SVN':7, 'EGT':8,'NIN':9}
keys = ['ZRO' , 'ONE' ,'TWO' , 'THR','FOR' ,'FIV','SIX','SVN', 'EGT','NIN']

# 카운팅 정렬
for _ in range(1,T+1):
    tc,N = input().split()
    S = list(input().split())
    str_cnt = [0] * len(keys)

    for number in S:
        for i in range(len(keys)):
            if number == keys[i]:
                str_cnt[i] += 1
                break

    result = []
    for j in range(len(keys)):
        for _ in range(str_cnt[j]):
            result.append(keys[j])
    print('{}'.format(tc))
    print(result)