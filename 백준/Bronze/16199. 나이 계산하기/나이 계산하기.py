y,m,d = map(int,input().split())
sy,sm,sd = map(int,input().split())
# 만 나이
if sm > m or (sm == m and sd >=d):
    print(sy-y)
else:
    print(sy-y-1)
# 세는 나이
print(sy-y+1)
# 연 나이
print(sy-y)