def solution(sequence):
    answer = -1e9
    
    dp = [[0,0] for _ in range(len(sequence))]
    dp[0][0], dp[0][1] = sequence[0] * -1, sequence[0]
    
    answer = max(answer,max(dp[0]))
    
    for idx, val in enumerate(sequence):
        if idx == 0:
            continue
            
        # 펄스 수열이므로 계속 변경해줘야 한다.
        if idx % 2 == 0:
            dp[idx][0] = max(dp[idx-1][0],0) + sequence[idx] * -1
            dp[idx][1] = max(dp[idx-1][1],0) + sequence[idx]
        else:
            dp[idx][0] = max(dp[idx-1][0],0) + sequence[idx] 
            dp[idx][1] = max(dp[idx-1][1],0) + sequence[idx] * -1
        answer = max(answer,max(dp[idx]))
        
    return answer