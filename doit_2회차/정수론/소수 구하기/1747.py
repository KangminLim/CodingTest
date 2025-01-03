# 소수팰린드롬
import math
N = int(input())
A = [0] * (10000001)

for i in range(2,len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A))+1)): # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i): # 배수 지우기
        A[j] = 0

def isPalindrome(target):
    temp = list(str(target))
    s = 0
    e = len(temp)-1
    while (s<e):
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = N

while True:
    if A[i] != 0:
        result = A[i]
        if isPalindrome(result):
            print(result)
            break
    i += 1
