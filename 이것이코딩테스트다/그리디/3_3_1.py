# 숫자 카드 게임(min()사용)
n,m = map(int,input().split())
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)