def solution(s):
    slst = list(map(int,s.split()))
    answer =  str(min(slst)) + ' ' + str(max(slst))
    return answer