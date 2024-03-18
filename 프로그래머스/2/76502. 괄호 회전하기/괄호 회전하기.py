def braceket(s):
    stack = []
    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if stack[-1] == '(' and ch == ')':
                stack.pop()
            elif stack[-1] == '{' and ch == '}':
                stack.pop()
            elif stack[-1] == '[' and ch == ']':
                stack.pop()
            else:
                stack.append(ch)
    return True if len(stack) == 0 else False

def solution(s):
    answer = 0
    for i in range(len(s)):
        new_s = s[i:]+ s[:i]      
        if braceket(new_s):
            answer += 1
    return answer
            

     