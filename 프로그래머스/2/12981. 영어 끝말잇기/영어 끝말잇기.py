def solution(n, words):
    stack = []
    for i in range(len(words)):
        if not stack:
            stack.append(words[i])
        else:
            print(stack[-1][-1],words[i][0])
            if stack[-1][-1] == words[i][0] and words[i] not in stack:
                stack.append(words[i])
            else:
                return [len(stack)%n + 1, len(stack)//n+1]
    return [0,0]