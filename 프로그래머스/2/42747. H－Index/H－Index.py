def solution(citations):
    citations.sort(reverse=True)
    length = len(citations)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    if max(citations) == 0:
        return 0 
    return length