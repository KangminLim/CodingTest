def solution(record):
    answer = []
    id_dict = {}
    id_lst = []
    for r in record:
        # 참가
        if r[:5] == 'Enter':
            state, user_id, name = r.split(' ')
            id_dict[user_id] = name
            id_lst.append((user_id, True))
        # 퇴장
        elif r[:5] == 'Leave':
            state, user_id = r.split(' ')
            id_lst.append((user_id, False))

        # 변경
        else:
            state, user_id, name = r.split(' ')
            id_dict[user_id] = name
    
    for i in range(len(id_lst)):
        
        if id_lst[i][1]: # 들어옴
            tmp = f'{id_dict[id_lst[i][0]]}님이 들어왔습니다.'
        else: # 나감 
            tmp = f'{id_dict[id_lst[i][0]]}님이 나갔습니다.'
            
        answer.append(tmp)
    return answer