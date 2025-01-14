def solution(N, stages):
    answer = []
    stages.sort()
    for i in range(1,N+1):
        tmp = 0
        for j in range(len(stages)):
            if stages[j] == i:
                tmp += 1
            elif stages[j] > i:
                break
        answer.append((i,tmp/len(stages)))
        stages = stages[j:]
    answer.sort(key = lambda x:(-x[1]))
    
    result = []
    for idx, val in answer:
        result.append(idx)
    
    return result