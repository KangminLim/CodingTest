answer = ''
cnt = 0
def dfs(word,q):
    global cnt, answer
    if q == word:
        answer = cnt
        return 
    if len(q) == 5:
        return 
    
    alpha = ['A','E','I','O','U']
    for i in range(5):
        cnt += 1
        q.append(alpha[i])
        dfs(word,q)
        q.pop()
    return 

def solution(word):
    word = list(word)
    q = []
    dfs(word,q)
    return answer