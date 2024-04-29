def solution(elements):
    answer = 0
    aset = set()
    elen = len(elements)
    elements = 2 * elements
    for i in range(elen):
        for j in range(elen):
            # print(elements[i:j+1])
            tmp = sum(elements[i:i+j+1])
            aset.add(tmp)
        
    return len(aset)