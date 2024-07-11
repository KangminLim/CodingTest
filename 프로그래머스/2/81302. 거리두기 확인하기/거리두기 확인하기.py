from collections import deque
def solution(places):
    answer = []
    def bfs(si,sj,arr):
        q = deque()
        q.append((si,sj,0))
        v = [[False] * 5 for _ in range(5)]
        v[si][sj] = True
        
        while q:
            ci,cj,dist = q.popleft()
            if dist > 2: break
            for ni,nj in ((ci-1,cj),(ci,cj+1),(ci+1,cj),(ci,cj-1)):
                if 0<=ni<5 and 0<=nj<5 and not v[ni][nj]: 
                    if arr[ni][nj] == 'O' and dist==0:                    
                        q.append((ni,nj,dist+1))
                    if dist<=2 and arr[ni][nj] == 'P':
                        return False
        return True
                    
    for place in places:
        partition = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    partition.append((i,j))
        flag = True
        for ti,tj in partition:
            if not bfs(ti,tj,place):
                answer.append(0)
                flag = False
                break
        if flag: answer.append(1)
        
    return answer