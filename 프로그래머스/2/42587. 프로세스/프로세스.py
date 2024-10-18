def solution(priorities, location):
    answer = 0 
    stack = []
    for idx,val in enumerate(priorities):
        stack.append((idx,val))
    while stack:
        if stack[0][1] == max(priorities):
            priorities.pop(0)
            cur_n, cur = stack.pop(0)
            answer += 1
            if cur_n == location:
                return answer
        else:
            cur_n, cur = stack.pop(0)
            stack.append((cur_n,cur))
            priorities.append(priorities.pop(0))

        
    return answer