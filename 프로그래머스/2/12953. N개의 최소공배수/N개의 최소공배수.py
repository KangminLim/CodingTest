import math
def solution(arr):
    answer = 0 
    for i in arr:
        # 초깃값
        if answer == 0:
            answer = i
        else: 
            answer = (answer*i) // math.gcd(answer,i)
    return answer