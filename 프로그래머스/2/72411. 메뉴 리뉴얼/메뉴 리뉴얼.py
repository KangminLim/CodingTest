from itertools import combinations
def solution(orders, course):
    answer = []
    odict = {}
    for order in orders:
        order = sorted(order)
        for c in course:
            for comb in combinations(order,c):   
                tmp = ''
                for ch in comb:
                    tmp += ch
                if tmp not in odict:
                    odict[tmp] = 1
                else:
                    odict[tmp] += 1
    
    olst = sorted(odict.items(),key=lambda x:(-x[1],x[0]))
    for k,v in olst:
        if v == 1:
            odict.pop(k)

    olst = sorted(odict.items(),key=lambda x:(len(x[0]),-x[1]))

    cur_len,cur_val = len(olst[0][0]),olst[0][1]
    
    for i in range(len(olst)-1):
        if cur_len == len(olst[i+1][0]):
            if cur_val > olst[i+1][1]:
                odict.pop(olst[i+1][0])
        else:
            cur_len,cur_val = len(olst[i+1][0]),olst[i+1][1]
    
    olst = sorted(odict.items(),key=lambda x:(x[0]))
    
    for k,v in olst:
        answer.append(k)
        
    return answer