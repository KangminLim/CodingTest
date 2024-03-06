def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    result = []
    
    for idx, answer in enumerate(answers):
        if answer == first[idx%len(first)]:
            scores[0] += 1
        if answer == second[idx%len(second)]:
            scores[1] += 1
        if answer == third[idx%len(third)]:
            scores[2] += 1
            
    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx+1)
            
    return result