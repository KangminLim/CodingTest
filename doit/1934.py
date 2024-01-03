#최소공배수 구하기공
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b) # 재귀 형태로 구현

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    result = a*b/gcd(a,b)
    print(int(result))
