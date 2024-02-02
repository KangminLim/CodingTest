# 곱하기 혹은 더하기
S = list(input())
answer = 0
for i in S:
    if int(i) == 0:
        continue
    if answer == 0:
        answer += int(i)
    else:
        answer *= int(i)

print(answer)