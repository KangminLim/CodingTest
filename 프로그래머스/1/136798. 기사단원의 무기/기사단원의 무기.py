def solution(number, limit, power):
    answer = 0
    weapon = []
    for i in range(1,number+1):
        nums = []
        for j in range(1,int(i**(1/2))+1):
            if i%j==0:
                nums.append(j)
                if i // j  != j:
                    nums.append(i//j)
        num = len(set(nums))
        if num > limit:
            weapon.append(power)
        else:
            weapon.append(num)
    answer = sum(weapon)

    return answer