def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = True
    for v in nums:
        needed_number = target - v
        # if needed_number in nums를 하면 O(N^2)
        if needed_number in memo:
            return True
        return False
# 같은 원소를 쓸 떄 예외 처리 해보기

two_sum(nums=[4,1,9,7,5,3,16], target=14)