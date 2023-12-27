def merge_sort(s,e):
    if e-s<1: return
    m = int(s+(e-s)/2)
    merge_sort(s,m)
    merge_sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]
        
    k = s
    idx1 = s
    idx2 = m + 1
    while idx1 <= m and idx2 <= e: 
        if tmp[idx1] > tmp[idx2]:
            A[k] = tmp[idx2]
            k += 1 
            idx2 += 1 
        else:
            A[k] = tmp[idx1]
            k += 1
            idx1 += 1
    
    while idx1 <= m: # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        A[k] = tmp[idx1]
        k += 1
        idx1 += 1
    while idx2 <= e:
        A[k] = tmp[idx2]
        k += 1 
        idx2 += 1
        
N = int(input())
A = [0] * int(N+1)
tmp = [0] * int(N+1)

for i in range(1,N+1):
    A[i] =int(input())
    
merge_sort(1,N)

for i in range(1,N+1):
    print(str(A[i]))