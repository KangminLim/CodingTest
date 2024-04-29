def solution(sequence, k):
    answer = []
    slen = len(sequence)
    mn = 10000001
    # sequence를 순회
    tlst = []
    s,e,tmp = 0,0,sequence[0]
    while s<=e<slen:
        # cnt를 추가하면서 최소 길이 인덱스 찾기
        if tmp == k:
            if e-s+1 < mn:
                mn = e-s+1
                answer = [s,e]
            tmp -= sequence[s]
            s += 1
        elif tmp > k:
            tmp -= sequence[s]
            s += 1
        elif tmp <k:
            e += 1
            if e < slen:
                tmp += sequence[e]
    return answer