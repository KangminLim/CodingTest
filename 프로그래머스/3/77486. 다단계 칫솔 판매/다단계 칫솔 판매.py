def solution(enroll, referral, seller, amount):
    answer = []
    total = {}
    graph = {}
    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
        total[enroll[i]] = 0
        
    left = 0
    
    def dfs(name,money):
        left = int(money*0.1)
        total[name] += money - left
        
        if graph[name] == '-' or left == 0:
            return
        else:
            dfs(graph[name], left)
            
    for i in range(len(seller)):
        dfs(seller[i],int(amount[i] * 100))
        
    for e in enroll:
        answer.append(total[e])
    
    return answer