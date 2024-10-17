def solution(clothes):
    answer = 1
    cdict = {}
    for clothe in clothes:
        name, genre = clothe
        if genre not in cdict:
            cdict[genre] = [name]
        else:
            cdict[genre].append(name)
    tlst = []
    for key in cdict:
        answer *= len(cdict[key])+1
    answer -=1 
            
    return answer