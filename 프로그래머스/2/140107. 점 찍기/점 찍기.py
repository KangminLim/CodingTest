import math
def solution(k, d): 
    answer = 0
    for x in range(0, d+1,k):
        # y값 구하기 
        y = math.sqrt(d**2-x**2)
        # 각각 x마다 구할 수 있는 y좌표
        answer += y//k + 1
    return answer    
    
        