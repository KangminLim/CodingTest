from collections import deque
def solution(progresses, speeds):
    answer = []
    # q = deque(progresses)
    while progresses:
        cur = progresses.pop(0)
        cur_speed = speeds.pop(0)
        days = 0
        while cur < 100:
            cur += cur_speed
            days += 1
            if cur >= 100:
                tmp = 1
                while progresses:
                    if progresses[0] + speeds[0] * days >= 100:
                        progresses.pop(0)
                        speeds.pop(0)
                        tmp += 1
                    else:
                        break
                answer.append(tmp)
        
    return answer