# 최솟값을 만드는 괄호 배치 찾기
answer = 0
A = list(map(str, input().split('-')))

def mySum(i): # -로 나뉜 그룹들의 합을 구하는 함수
    sum = 0
    temp = str(i).split('+')
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i==0:
        answer += temp
    else:
        answer -= temp

print(answer)