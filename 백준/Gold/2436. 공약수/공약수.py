import math
gcd, lcm = map(int,input().split())
mul = gcd*lcm
tlst = []
for i in range(1,int(math.sqrt(mul)+1)):
    if mul % i == 0:
        tlst.append((i,int(mul/i)))
answer = []
for i in range(len(tlst)):
    num1,num2 = tlst[i]

    if math.gcd(num1,num2) == gcd:
        answer.append((num1,num2))
answer.sort(key=lambda x: (x[0]+x[1],x[0],x[1]))
print(answer[0][0],answer[0][1])