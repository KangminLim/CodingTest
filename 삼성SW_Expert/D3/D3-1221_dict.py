T = int(input())


keys = ['ZRO' , 'ONE' ,'TWO' , 'THR','FOR' ,'FIV','SIX','SVN', 'EGT','NIN']

# 카운팅 정렬
for _ in range(1,T+1):
    tc,N = input().split()
    dic = {'ZRO': 0,
           'ONE': 1,
           'TWO': 2,
           'THR': 3,
           'FOR': 4,
           'FIV': 5,
           'SIX': 6,
           'SVN': 7,
           'EGT': 8,
           'NIN': 9,
           }
    S = input().split()
    S.sort(key=lambda num:dic[num])
    print('{} {}'.format(tc,' '.join(S)))