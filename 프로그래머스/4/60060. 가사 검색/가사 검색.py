from bisect import bisect_left, bisect_right

def count_by_range(a,left_value,right_value):
    right_idx = bisect_right(a,right_value)
    left_idx = bisect_left(a,left_value)
    return right_idx - left_idx

def solution(words, queries):
    answer = []
    
    arr = [[] for _ in range(10001)]
    re_arr = [[] for _ in range(10001)]
    
    # 모든 단어를 접미사 와일드카드 배열, 접두사를 와일드카드 배열에 각각 삽입
    for word in words:
        arr[len(word)].append(word)
        re_arr[len(word)].append(word[::-1])

    for i in range(10001): # 이진 탐색을 위한 정렬
        arr[i].sort()
        re_arr[i].sort()
    
    for q in queries:
        if q[0] != '?': 
            res = count_by_range(arr[len(q)], q.replace('?','a'), q.replace('?','z'))
        else:
            res = count_by_range(re_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(res)
    return answer