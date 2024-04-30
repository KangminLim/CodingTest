# n x m , (x,y) -k> (r,c)
def solution(n, m, x, y, r, c, k):
    # 이동할 수 없으면 impossible
    # k = 1, (1,1) -> (5,1)
    distance = abs(r-x) + abs(c-y)
    if distance > k :
        return "impossible"
    # k = 4, (1,1) -> (2,1), lr,rl,ud,du
    if (distance - k) % 2:
        return "impossible"
    
    # dlru 
    down = max(r-x,0)
    left = max(y-c,0)
    right = max(c-y,0)
    up = max(x-r,0)
    pair = (k-distance) // 2
    # 이동할 수 있으면 사전 순으로 가장 빠른 경우를 return
    answer = ''
    for _ in range(k):
        if (down or pair) and x < n: 
            answer += 'd'
            if down : 
                down -= 1
            else:
                pair -= 1
                up += 1
            x += 1
        elif (left or pair) and y > 1:
            answer += 'l'
            if left : 
                left -= 1
            else:
                pair -= 1
                right += 1
            y -= 1
        elif (right or pair) and y < m:
            answer += 'r'
            if right:
                right -= 1
            else:
                pair -= 1
                left += 1
            y += 1
        else: # up
            answer += 'u'
            if up:
                up -=1
            else:
                pair -= 1
                down += 1
            x -= 1
        
    
    return answer