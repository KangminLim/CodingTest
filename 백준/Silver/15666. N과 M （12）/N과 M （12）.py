N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
sequence = []

def bt(depth, start_index):
    if depth == M:
        print(' '.join(map(str,sequence)))
        return

    prev = -1
    for i in range(start_index,N):
        if prev != lst[i]: # 이전 숫자와 다를 때만 선택
            sequence.append(lst[i])
            bt(depth+1,i)
            sequence.pop()
            prev = lst[i]
bt(0,0)