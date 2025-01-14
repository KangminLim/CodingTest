# 18310
# 시간초과
import sys
input = sys.stdin.readline
# N = int(input())
# lst = list(map(int,input().split()))
# mn = int(1e9)
# ans = max(lst)+1
# for i in range(1,max(lst)+1):
#     tmp = 0
#     for j in range(N):
#         tmp += abs(i-lst[j])
#     if mn > tmp:
#         mn = tmp
#         ans = i
# print(ans)

N = int(input())
lst = list(map(int,input().split()))
lst.sort()
print(lst[(N-1)//2])