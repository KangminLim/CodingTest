from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    def bfs(begin,target,words):
        q = deque()
        q.append((begin,0))
        while q:
            cur, cnt = q.popleft()
            if cur == target:
                return cnt

            for word in words:
                count = 0
                for i in range(len(cur)):
                    if cur[i] != word[i]:
                        count += 1
                if count == 1:
                    q.append((word,cnt+1))
    answer = bfs(begin,target,words)
    return answer