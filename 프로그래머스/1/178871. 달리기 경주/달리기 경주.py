def solution(players, callings):
    
    # 인덱스로 직접 접근 => 시간 초과
    # for call in callings:
    #     cidx = players.index(call)
    #     tmp1 = players[cidx-1]
    #     tmp2 = players[cidx]
    #     players[cidx-1] = tmp2
    #     players[cidx] = tmp1
    # return players
    
    pdict = {}
    for idx, val in enumerate(players):
        pdict[val] = idx
        
    for call in callings:
        idx = pdict[call]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]
        pdict[players[idx-1]] = idx-1
        pdict[players[idx]] = idx
        
    return players