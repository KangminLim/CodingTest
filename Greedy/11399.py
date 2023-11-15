N = int(input())
lst = list(map(int, input().split()))
lst.sort()
result= 0
new_res = 0
for i in range(N):
    result += lst[i]
    new_res += result
print(new_res)