def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = 1
    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
    return False

two_sum(nums= [4,1,3,8,6,2,3,16], target=14)