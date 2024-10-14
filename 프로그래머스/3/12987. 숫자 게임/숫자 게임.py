def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    i = 0
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1
    return answer