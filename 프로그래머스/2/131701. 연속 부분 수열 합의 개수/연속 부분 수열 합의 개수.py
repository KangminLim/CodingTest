def solution(elements):
    tset = set()
    e_len =len(elements)
    elements = elements*2
    for i in range(e_len):
        # temp = elements[i]
        # tset.add(temp)
        for j in range(e_len):
            temp = sum(elements[j:j+1+i])
            tset.add(temp)
    return len(tset)