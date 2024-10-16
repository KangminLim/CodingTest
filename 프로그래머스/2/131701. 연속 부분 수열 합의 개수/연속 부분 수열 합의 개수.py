def solution(elements):
    answer = 0
    l = len(elements)
    elements = 2*elements
    aset = set()
    for j in range(1,l+1): 
        for i in range(l):
            aset.add(sum(elements[i:i+j]))
    return len(aset)