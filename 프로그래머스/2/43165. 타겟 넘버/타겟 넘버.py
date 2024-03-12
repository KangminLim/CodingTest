def solution(numbers, target):
    answer = 0
    def dfs(n,sm):
        nonlocal answer 
        if n==len(numbers):
            if sm ==target:    
                answer +=1
            return
        dfs(n+1,sm+numbers[n])
        dfs(n+1,sm-numbers[n])
    dfs(0,0)
    return answer