N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
result_lst =[]
for i in range(len(lst)):
    result_lst.append((i+1)*lst[i])
print(max(result_lst))