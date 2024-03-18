def solution(s):
    answer = -1
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return 0
    else: return 1