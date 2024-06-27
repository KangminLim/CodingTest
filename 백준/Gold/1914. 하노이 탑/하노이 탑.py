def hanoi(N,start,mid,end):
    if N == 1:
        print(start,end)
        return

    hanoi(N-1,start,end,mid) # 1단계 (1->2)
    print(start,end) # 2단계 (1의 마지막 원반 -> 3)
    hanoi(N-1,mid,start,end) # 3단계 (2->3)

N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(N,1,2,3)