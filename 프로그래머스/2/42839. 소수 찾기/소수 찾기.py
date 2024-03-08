
import math
from itertools import permutations
def prime_n(n):
    if n == 1 or n == 0:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
        
    return True

def solution(numbers):
    lst = list(numbers)
    nums = set()
    for i in range(1,len(numbers)+1):
        perlst = permutations(lst,i)
        for perm in perlst:
            num = int(''.join(perm))
            nums.add(num)
    cnt = 0
    for n in nums:
        if prime_n(n):
            cnt +=1
    return cnt
    