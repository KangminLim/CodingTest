def solution(N, number):

    dp = [set() for _ in range(9)]
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if a != 0 and b != 0: dp[i].add(a//b)
        if number in dp[i]: return i
    return -1