def solution(scores):
    
    answer = 1
    h_a, h_b = scores[0]
    h_score = h_a + h_b
    
    scores.sort(key = lambda x:(-x[0],x[1]))
    maxb = 0

    for a, b in scores:
        if h_a < a and h_b < b:
            return -1
        if b >= maxb:
            maxb = b
            if a + b > h_score:
                answer += 1
    return answer