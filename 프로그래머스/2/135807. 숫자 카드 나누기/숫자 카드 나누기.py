import math

def get_gcd(arr):
    tmp = math.gcd(arr[0],arr[1]) 
    if len(arr) < 2:
        return tmp
    
    for i in range(2,len(arr)):
        tmp = math.gcd(tmp,arr[i]) 
    return tmp
    
def simul(gcd,arr):
    for num in arr:
        if num % gcd == 0:
            return False
    return True
    

def solution(arrayA, arrayB):
    if len(arrayA) == 1:
        a = arrayA[0]
    else:    
        a = get_gcd(arrayA)
    if len(arrayB) == 1:
        b = arrayB[0]
    else:
        b = get_gcd(arrayB)
    # 1번 상황
    if not simul(a,arrayB): a = 0
    
    # 2번 상황
    if not simul(b,arrayA): b = 0
    
    return max(a,b)