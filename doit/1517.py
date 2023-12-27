result = 0 

def merge_sort(s, e):
    global result
    if e - s < 1 : return
    m = int(s + (e-s)/ 2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s 
    idx1 = s
    idx2 = m+1
    while idx1 <= m and idx2 <= e: # 두 그룹을 병합하는 로직
        if tmp[idx1] > tmp[idx2]: 
            A[k] = tmp[idx2]
            result = result + idx2 - k # 뒤쪽 데이터값이 더 작다면 결과값 업데이트
            k += 1
            idx2 += 1
        else:
            A[k] =tmp[idx1]
            k += 1
            idx1 += 1
    while idx1 <= m:
        A[k] = tmp[idx1]
        k += 1
        idx1 += 1
    while idx2 <=e:
        A[k] = tmp[idx2]
        k += 1
        idx2 += 1

N =int(input())
A = list(map(int,input().split()))
A.insert(0,0) #인덱스에 요소 추가 
tmp = [0] * int(N+1)
merge_sort(1,N)
print(result)
