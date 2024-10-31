def mod_pow(A,B,C):
    if B == 0:
        return 1%C
    elif B == 1:
        return A%C

    temp = mod_pow(A,B//2,C)
    if B%2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * A) % C

A,B,C = map(int,input().split())
print(mod_pow(A,B,C))