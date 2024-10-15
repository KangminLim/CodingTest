def solution(genres, plays):
    answer = []
    # 1. 가장 많이 재생된 장르 수록
    gdict = {}
    for i in range(len(genres)):
        if genres[i] not in gdict:
            gdict[genres[i]] = plays[i]
        else:
            gdict[genres[i]] += plays[i]
    # 2. 장르 내에서 많이 재생된 노래 먼저 수록
    pdict = {}
    for idx,val in enumerate(genres):
        if val not in pdict:
            pdict[val] = [(plays[idx],idx)]
        else:
            pdict[val].append((plays[idx],idx))
    # 3. 장르 내에서 재생 회수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록
    glst = sorted(gdict.items(),key = lambda x: -x[1])
    
    for i in range(len(glst)):
        genre, _ = glst[i]
        plst = pdict[genre]
        plst.sort(key=lambda x: (-x[0],x[1]))
        for j in range(0,min(2,len(plst))):
            answer.append(plst[j][1])
    
    return answer
