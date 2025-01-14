# 10825
N = int(input())

lst = []
for _ in range(N):
    name, kor, eng, mth = input().split()
    lst.append((name,int(kor),int(eng),int(mth)))
lst.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(N):
    print(lst[i][0])