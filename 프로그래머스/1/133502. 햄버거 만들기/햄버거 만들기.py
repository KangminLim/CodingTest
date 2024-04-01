def solution(ingredient):
    
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        # 뒤부터 확인하면서 빼려고 
        if s[-4:] == [1,2,3,1]:
            answer += 1
            for _ in range(4):
                s.pop()
            
    return answer