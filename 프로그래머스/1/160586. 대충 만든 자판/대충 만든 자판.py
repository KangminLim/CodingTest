def solution(keymap, targets):
    answer = []
    km = {}
    
    for key in keymap:
        for i,k in enumerate(key):
            km[k] = min(i+1,km[k]) if k in km else i+1
            
    for target in targets:
        c = 0
        for t in target:
            if t not in km:
                answer.append(-1)
                break
            c += km[t]
        else: # for else 에서 break를 사용하면 else를 사용해줘야함
            answer.append(c)
    return answer
            