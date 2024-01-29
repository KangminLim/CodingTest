N = int(input())
lst = list(map(int,input().split()))
new_sum = 0
new_avg = 0
for i in lst:
    new_sum += (i / max(lst) * 100)

new_avg = new_sum / len(lst)
print(new_avg)