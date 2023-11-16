from collections import deque
# 암시적 그래프 표현
def numIslands(grid):
    number_of_islands = 0
    m=len(grid)
    n=len(grid[0])
    visited=[[False]*n for _ in range(m)]

    def bfs(x,y):
        # 동서남북
        dx = [-1, 1,0,0]
        dy = [0,0,-1,1]
        visited[x][y] = True
        queue = deque()
        queue.append((x,y))
        while queue:
            cur_x, cur_y = queue.popleft()
            # 상하좌우
            for i in range(4):
                next_x = cur_x +dx[i]
                next_y = cur_y +dy[i]
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] =='1' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_y,next_y))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i,j)
                number_of_islands += 1
    return number_of_islands




print(numIslands(grid=[
    ['1','1','0','0','0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]))
