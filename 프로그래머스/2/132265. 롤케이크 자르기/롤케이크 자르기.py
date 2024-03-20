from collections import Counter
def solution(topping):
    answer = 0
    left = Counter(topping)
    right = set()
    for i in topping:
        left[i] -= 1
        right.add(i)
        
        if left[i] == 0:
            left.pop(i)
        
        if len(left) == len(right):
            answer += 1
        
    return answer