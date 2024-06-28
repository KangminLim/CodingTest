


def solution(enroll, referral, seller, amount):
    
    total, graph, answer  = {}, {}, [] 
    
    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
        total[enroll[i]] = 0

    left = 0

    def dfs(name,money):
        left = int(money*0.1)
        total[name] += money - left

        # 종료 조건 center 하위 노드 or 1원 미만
        if graph[name] == "-" or left ==0:
            return
        # 추천인에게 올라가기 
        else:
            dfs(graph[name],left)
    
    for i in range(len(seller)):
        dfs(seller[i],amount[i] * 100)
    for e in enroll:
        answer.append(total[e])
    
    return answer