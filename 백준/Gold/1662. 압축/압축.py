import sys

S = str(input())
length, mul = 0, 0

stack = []
ans = 0
for i in range(len(S)):
    if S[i] == '(':
        stack.append((length-1,mul))
        length = 0
    elif S[i] == ')':
        length_,mul_ = stack.pop()
        length = mul_ * length + length_
    else:
        length += 1
        mul = int(S[i])
print(length)