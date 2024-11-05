def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        s = ''
        for ch in tree:
            if ch in skill:
                s += ch
        if skill[:len(s)] == s:
            answer += 1
                
    return answer