from collections import Counter
def solution(participant, completion):
    participant_dict = Counter(participant)
    completion_dict = Counter(completion)

    answer = (participant_dict - completion_dict)
    return [x for x in answer.keys()][0]
