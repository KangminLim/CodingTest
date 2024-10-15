def can_cross(stones,k,mid):
    cnt = 0
    for stone in stones:
        if stone - mid < 0:
            cnt += 1
            if cnt == k:
                return False
        else:
            cnt = 0
            
    return True

def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0
    
    while left<=right:
        mid = (left+right)//2
        if can_cross(stones,k,mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        
    return answer
                
        