def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, val in enumerate(citations):
        if idx >= val:
            return idx
    if max(citations) == 0:
        return 0
    
    return len(citations)