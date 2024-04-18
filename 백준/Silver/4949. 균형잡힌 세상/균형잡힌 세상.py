while True:
    word = input()
    stack = []
    if word =='.':
        break
    for w in word:
        if w=='(' or w=='[':
            stack.append(w)
        elif w==')' :
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(w)
                break
        elif w==']':
            if len(stack)!=0 and stack[-1] =='[':
                stack.pop()
            else:
                stack.append(w)
                break
    if stack:
        print('no')
    else:
        print('yes')