#구간합구하기 4
N, M = map(int,input().split())
lst = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for i in lst:
    temp += i
    prefix_sum.append(temp)

for i in range(M):
    s,e = map(int,input().split())
    print(prefix_sum[e] - prefix_sum[s-1])