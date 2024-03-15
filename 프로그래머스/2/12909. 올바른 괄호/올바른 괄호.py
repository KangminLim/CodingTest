def solution(s):
    if s[0] == ')':
        return False
    
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif stack and s[i] ==')':
            stack.pop()
    if stack:
        return False
    
    return True