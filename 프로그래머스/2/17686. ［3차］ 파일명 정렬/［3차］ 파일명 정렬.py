def solution(files):
    answer = []
    
    for file in files:
        HEAD, NUMBER, TAIL = '', '', ''
        # NUMBER 만나기 전
        Flag = False
        for i in range(len(file)):
            # NUMBER 처리
            if file[i].isdigit():
                NUMBER += file[i]
                Flag = True
            # HEAD 처리 
            elif not Flag:
                HEAD += file[i]
            # TAIL 처리
            else:
                TAIL += file[i:]
                break
        answer.append((HEAD,NUMBER,TAIL))
    answer.sort(key=lambda x : (x[0].upper(),int(x[1])))
    answer = [''.join(a) for a in answer]
    return answer