def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    check = -1
    for idx in range(len(targets)):
        if check <= targets[idx][0]:
            check = targets[idx][1]
            answer += 1
    return answer