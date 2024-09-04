def solution(bandage, health, attacks):
    answer = 0
    time = 0
    cur = 0
    max_health = health
    t, x, y = bandage
    while attacks:
        time += 1
        cur += 1
        flag = True
        
        for attack in attacks:
            at, ap = attack
            if time != at:
                break
            else:
                flag = False
                health -= ap
                cur = 0
                attacks.pop(0)
        if flag:
            health = min(max_health,health+x)
            if cur == t:
                cur = 0
                health = min(max_health,health+y)
        if health <= 0: 
            return -1
    if health > 0:
        return health
    else:
        return -1