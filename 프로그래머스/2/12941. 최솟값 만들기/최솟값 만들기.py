def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    l = len(A)
    for i in range(l):
        answer += A[i] * B[i]
    return answer