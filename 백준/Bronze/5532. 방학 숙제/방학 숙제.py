L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

for day in range(1,L+1):
    A = max(0, A-C)
    B = max(0, B-D)
    if A == 0 and B == 0:
        break
print(L-day)

