def solution(s):
    # 문자열 dict
    s_dict = { 'zero': 0,
             'one': 1,
             'two': 2,
             'three': 3,
             'four': 4,
             'five': 5,
             'six': 6,
             'seven': 7,
             'eight': 8,
             'nine': 9}
    temp = ''
    answer = ''
    # s를 순회
    for ch in s:
        if ch.isalpha():
            temp += ch
            if temp in s_dict:
                answer += str(s_dict[temp])
                temp = ''
        elif ch.isdigit():
            answer += str(ch)
    
    return int(answer)
    