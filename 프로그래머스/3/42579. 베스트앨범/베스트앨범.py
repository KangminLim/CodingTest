def solution(genres, plays):
    answer = []
    total_dict = {}
    genre_dict = {}
    
    for i in range(len(genres)):
        # 장르 합
        if genres[i] not in total_dict:
            total_dict[genres[i]] = plays[i]
        else:
            total_dict[genres[i]] += plays[i]
        # 장르 정보 
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = [[plays[i],i]]
        else:
            genre_dict[genres[i]].append([plays[i],i])
    
    genre_rank = sorted(total_dict, key=total_dict.get, reverse=True)
    
    for x in genre_rank:
        play_rank = sorted(genre_dict[x], key=lambda x:(-x[0],x[1]))
        
        if len(play_rank) == 1:
            answer.append(play_rank[0][1])
        else:
            for i in range(2):
                answer.append(play_rank[i][1])
    
    return answer