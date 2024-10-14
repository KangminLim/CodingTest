def solution(s):
    answer = -1
    stack = []
    i = 0 
    while i != len(s):
        if not stack:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else: 
            stack.append(s[i])
        i += 1
    if stack:
        return 0
    return 1