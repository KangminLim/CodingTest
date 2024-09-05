def solution(friends, gifts):
    N = len(friends)
    
    fdict = {}
    for i in range(N):
        fdict[friends[i]] = i
        
    # 주고 받은 선물 내역 표
    table = [[0] * N for _ in range(N)]
    # 선물 지수 저장
    gift_indices = [0] * N
    
    for gift in gifts:
        a, b = gift.split()
        idx1, idx2 = fdict[a], fdict[b]
        gift_indices[idx1] += 1
        gift_indices[idx2] -= 1
        table[idx1][idx2] += 1
    
    get_gift = [0] * N
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if table[i][j] > table[j][i]: # 준 게 더 많으면
                get_gift[i] += 1
            elif table[i][j] == table[j][i]: # 주고 받은게 같거나 둘 다 안주고 받았을 때      
                if gift_indices[i] > gift_indices[j]: # 선물 지수 크면 선물 받기
                    get_gift[i] += 1   
                    
    return max(get_gift)
    