expression = input()

parts = expression.split('-')
answer = 0
for i in parts[0].split('+'):
    answer += int(i)
for i in parts[1:]:
    for j in i.split('+'):
        answer -= int(j)
print(answer)

# expression = input("식을 입력하세요: ")

# # 빼기 기호를 기준으로 수식을 분리합니다.
# parts = expression.split('-')

# # 첫 번째 덩어리는 그대로 두고, 나머지 덩어리의 수들은 모두 빼기로 처리합니다.
# result = sum(map(int, parts[0].split('+')))
# for part in parts[1:]:
#     result -= sum(map(int, part.split('+')))

# print("최소 결과값:", result)
