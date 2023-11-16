# 접근 방법1
def longestConsecutive(nums):
    longest = 0
    num_dict = {}
    # nums에 있는 key값을 num_dict의 key값으로 넣기
    for num in nums:
        num_dict[num] = True
    # num_dict의 key값을 하나 하나 돌면서
    for num in num_dict:
        # num 앞의 수를 찾기 (중복 제거)
        if num-1 not in num_dict:
            cnt = 1
            target =  num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest
longestConsecutive([6,7,100,5,4,4]) #key값으로 4가 있어서 4중복 안됨


# for안에 있는 while문은 조건이 있으므로 시간복잡도를 높이지 않는다.
