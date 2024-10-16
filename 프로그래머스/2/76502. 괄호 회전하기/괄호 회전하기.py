def solution(s):
    ts = s
    answer = 0
    while True:
        flag = True
        stack = []
        for i in s:
            if not stack:
                if i == ']' or i == ')' or i == '}':
                    flag = False
                    break
                else:
                    stack.append(i)

            else:
                if i == '[' or i == '(' or i == '{':
                    stack.append(i)
                else:
                    if (stack[-1] == '[' and i == ']') or (stack[-1] == '{' and i == '}') or (stack[-1] == '(' and i == ')'):
                        stack.pop()
                    else:
                        flag = False
                        break
        if flag and not stack:
            answer += 1
        
        s = s[1:] + s[0]
        
        if s == ts:
            break
                    
    
    return answer

