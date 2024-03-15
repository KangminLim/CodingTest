def solution(genres, plays):
    answer = []
    N = len(genres)
    g_dict = {}
    t_dict = {}
    for i in range(N):
        if genres[i] not in g_dict:
            g_dict[genres[i]] = plays[i]
        else:
            g_dict[genres[i]] += plays[i]
        
        if genres[i] not in t_dict:
            t_dict[genres[i]] = [[plays[i],i]]
        else:
            t_dict[genres[i]].append([plays[i],i])
    
    genre_rank = sorted(g_dict, key=g_dict.get, reverse = True)
    
    for x in genre_rank:
        total_rank = sorted(t_dict[x], key= lambda x : (-x[0],x[1]))
        
        if len(total_rank) == 1:
            answer.append(total_rank[0][1])
        else:
            for i in range(2):
                answer.append(total_rank[i][1])
    return answer