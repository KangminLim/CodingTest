# 완전 탐색 - unique paths
# 도착점 2,6
def dfs(r,c):
    if r == 2 and c ==6:
        return 1
    unique_paths = 0
    if r+1 < 3:
        unique_paths += dfs(r+1,c)
    if c+1 < 7:
        unique_paths += dfs(r,c+1)
    return unique_paths

# 도착점 전
def dfs(r,c):
    if r==0 and c==0:
        return 1
    unique_paths =0
    if r-1>=0:
        unique_paths += dfs(r-1,c)
    if c-1>=0:
        unique_paths += dfs(r,c-1)
    return unique_paths

# dp - unique paths(dict) top-down
memo = {}
def dfs(r,c):
    if r==0 and c==0:
        memo[(r,c)] = 1
        return memo[(r,c)]
    unique_paths = 0
    if (r,c) not in memo:
        if r-1>=0:
            unique_paths += dfs(r-1,c)

        if c-1>=0:
            unique_paths += dfs(r,c-1)

        memo[(r,c)] = unique_paths
    return memo[(r,c)]

# dp list
def uniquePaths(m,n):
    memo = [[-1] * n for _ in range(m)]
    def dfs(r,c):
        if r==0 and c==0:
            memo[r][c] = 1
            return memo[r][c]
        unique_paths=0
        if memo[r][c] == -1:
            if r-1>=0:
                unique_paths += dfs(r-1,c)

            if c-1>=0:
                unique_paths += dfs(r,c-1)
            memo[r][c] = unique_paths
        return memo[r][c]
    return dfs(m-1,n-1)
print(uniquePaths(3,7))

#dp - bottom-up
def uniquePaths(m,n):
    memo = [[-1] * n for _ in range(m)]

    for r in range(m):
        memo[r][0]=1
    for c in range(n):
        memo[0][c] =1
    for r in range(1,m):
        for c in range(1,n):
            memo[r][c] = memo[r-1][c] + memo[r][c-1]
    return memo[m-1][n-1]
print(uniquePaths(3,7))