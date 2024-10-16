    # 123   1234
    # 223   2234
    # 333   3334
    #       4444
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        div,mod = divmod(i,n)
        answer.append(max(div,mod)+1)
    return answer