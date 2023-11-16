dct={'0001101':0, '0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,
     '0111011':7,'0110111':8,'0001011':9}

def solve():
    for st in arr:
        if '1' in st:
            e = len(st)-1
            while st[e] =='0':
                e-=1
            ans = []
            for i in range(e-55,e+1,7):
                ans.append(dct[st[i:i+7]])

            if (sum(ans[0:8:2])*3 + sum(ans[1:8:2]))%10 ==0:
                return sum(ans[0:8:2]) + sum(ans[1:8:2])
            return 0

T = int(input())
for TC in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = solve()
    print(f'#{TC} {ans}')
