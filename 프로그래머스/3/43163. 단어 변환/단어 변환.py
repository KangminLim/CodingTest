from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    return answer

def bfs(begin,target,words):
    queue = deque()
    queue.append([begin,0])
     
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        for word in words:
            count = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    count += 1
        
            if count == 1:
                queue.append([word, step+1])