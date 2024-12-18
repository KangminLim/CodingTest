S = str(input())
T = str(input())
flag = False
while len(T) >= len(S):

    if S == T:
        flag = True
        break

    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1][::-1]

if flag:
    print(1)
else:
    print(0)