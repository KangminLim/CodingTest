def possible(answer):
    for x,y,build in answer:
        if build == 0:
            if y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif build == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,build,operate =  frame
        if operate == 0:
            answer.remove([x,y,build])
            if not possible(answer):
                answer.append([x,y,build])
        if operate == 1:
            answer.append([x,y,build])
            if not possible(answer):
                answer.remove([x,y,build])
    answer.sort()
    return answer

