def solution(s):
    answer = True
    if s[0] == ')':
        return False
    stack = []
    for i in range(len(s)):
        if i == 0: 
            stack.append(s[i])
            continue
        if s[i] == '(':
            stack.append(s[i])
        elif stack and s[i] == ')':
            stack.pop()
            
    if stack:
        return False
    return True