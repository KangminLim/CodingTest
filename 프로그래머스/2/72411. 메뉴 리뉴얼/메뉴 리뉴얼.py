from itertools import combinations
def solution(orders, course):
    answer = []
    odict = {}
    for order in orders:
        for c in course:
            for comb in combinations(order,c):   
                tmp = ''
                for ch in comb:
                    tmp += ch
                if tmp not in odict:
                    odict[tmp] = 1
                else:
                    odict[tmp] += 1
    
    olst = odict.items()
    olst = sorted(olst,key=lambda x:(-x[1],x[0]))
    print(odict)
    for k,v in olst:
        if v == 1:
            odict.pop(k)
    print(odict)
    
    tmp = ''
#     for i in range(len(olst)-1):
#         if tmp == '':
#             tmp = olst[i][0]
        
#         if olst[i][1] == olst[i+1][1]:
#             tmp += olst[i][0]
#         else:
#             answer.append(tmp)
#             tmp = ''
        
    return answer